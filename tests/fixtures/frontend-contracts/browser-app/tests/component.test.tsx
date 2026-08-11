import { cleanup, fireEvent, render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { afterEach, describe, expect, it, vi } from "vitest";
import { App } from "../src/App";
import { DisposableRegistry, classifyMediaCapability, parseMessageEnvelope, safeNavigationUrl } from "../src/browser-contract";

afterEach(cleanup);

describe("frontend contract fixture", () => {
  it("moves focus when the representative view changes", async () => {
    render(<App />);
    await userEvent.click(screen.getByRole("button", { name: "Open details" }));
    await waitFor(() => expect(screen.getByRole("heading", { name: "Details ready" })).toBe(document.activeElement));
    await userEvent.click(screen.getByRole("button", { name: "Back" }));
    expect(screen.getByRole("heading", { name: "Representative flow" })).toBeTruthy();
  });

  it("renders capability state without assuming a permission outcome", async () => {
    render(<App />);
    fireEvent.click(screen.getByRole("button", { name: "Check camera capability" }));
    expect(await screen.findByText("Camera capability: unavailable")).toBeTruthy();
  });

  it("validates runtime envelopes and navigation protocols", () => {
    expect(parseMessageEnvelope({ schemaVersion: 1, message: "ready" })).toEqual({ schemaVersion: 1, message: "ready" });
    expect(parseMessageEnvelope({ schemaVersion: 2, message: "ready" })).toBeNull();
    expect(parseMessageEnvelope(null)).toBeNull();
    expect(parseMessageEnvelope({ schemaVersion: 1, message: "" })).toBeNull();
    expect(safeNavigationUrl("/details")?.pathname).toBe("/details");
    expect(safeNavigationUrl("https://attacker.invalid/path")).toBeNull();
    expect(safeNavigationUrl("javascript:alert(1)")).toBeNull();
    expect(safeNavigationUrl("http://[invalid")).toBeNull();
  });

  it("classifies capability fallbacks and disposes owned resources", async () => {
    const mediaDevices = { getUserMedia: vi.fn() };
    expect(await classifyMediaCapability({ mediaDevices }, false)).toBe("unavailable");
    expect(await classifyMediaCapability({ mediaDevices: undefined, permissions: undefined }, true)).toBe("unsupported");
    expect(await classifyMediaCapability({ mediaDevices }, true)).toBe("prompt");
    for (const state of ["granted", "denied", "prompt"] as const) {
      const permissions = { query: vi.fn().mockResolvedValue({ state }) };
      expect(await classifyMediaCapability({ mediaDevices, permissions }, true)).toBe(state);
    }
    const failingPermissions = { query: vi.fn().mockRejectedValue(new Error("unsupported query")) };
    expect(await classifyMediaCapability({ mediaDevices, permissions: failingPermissions }, true)).toBe("prompt");
    const unknownPermissions = { query: vi.fn().mockResolvedValue({ state: "unknown" }) };
    expect(await classifyMediaCapability({ mediaDevices, permissions: unknownPermissions }, true)).toBe("indeterminate");
    const dispose = vi.fn();
    const registry = new DisposableRegistry();
    const unregister = registry.add(dispose);
    expect(registry.size).toBe(1);
    unregister();
    expect(registry.size).toBe(0);
    registry.add(dispose);
    registry.disposeAll();
    expect(dispose).toHaveBeenCalledOnce();
    expect(registry.size).toBe(0);
  });

  it("attempts every owned cleanup and releases registrations when one disposer fails", () => {
    const registry = new DisposableRegistry();
    const failingDispose = vi.fn(() => { throw new Error("cleanup failed"); });
    const remainingDispose = vi.fn();
    registry.add(failingDispose);
    registry.add(remainingDispose);

    expect(() => registry.disposeAll()).toThrow(AggregateError);
    expect(failingDispose).toHaveBeenCalledOnce();
    expect(remainingDispose).toHaveBeenCalledOnce();
    expect(registry.size).toBe(0);
  });
});
