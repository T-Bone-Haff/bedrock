export type MediaCapability =
  | "unsupported"
  | "unavailable"
  | "prompt"
  | "granted"
  | "denied"
  | "indeterminate";

export interface MessageEnvelope {
  schemaVersion: 1;
  message: string;
}

interface NavigatorCapabilities {
  mediaDevices?: Pick<MediaDevices, "getUserMedia">;
  permissions?: Pick<Permissions, "query">;
}

export function parseMessageEnvelope(input: unknown): MessageEnvelope | null {
  if (typeof input !== "object" || input === null) return null;
  const row = input as Record<string, unknown>;
  if (row.schemaVersion !== 1 || typeof row.message !== "string" || row.message.trim() === "") return null;
  return { schemaVersion: 1, message: row.message };
}

export function safeNavigationUrl(input: string, base = window.location.origin): URL | null {
  try {
    const url = new URL(input, base);
    const baseUrl = new URL(base);
    return (url.protocol === "https:" || url.protocol === "http:") && url.origin === baseUrl.origin ? url : null;
  } catch {
    return null;
  }
}

export async function classifyMediaCapability(
  navigatorLike: NavigatorCapabilities,
  secureContext: boolean,
): Promise<MediaCapability> {
  if (!secureContext) return "unavailable";
  if (!navigatorLike.mediaDevices?.getUserMedia) return "unsupported";
  if (!navigatorLike.permissions?.query) return "prompt";
  try {
    const status = await navigatorLike.permissions.query({ name: "camera" });
    if (status.state === "granted" || status.state === "denied" || status.state === "prompt") return status.state;
  } catch {
    // Permission-query support varies; the capability can still be requested.
    return "prompt";
  }
  return "indeterminate";
}

export class DisposableRegistry {
  readonly #disposers = new Set<() => void>();

  add(dispose: () => void): () => void {
    this.#disposers.add(dispose);
    return () => this.#disposers.delete(dispose);
  }

  disposeAll(): void {
    const disposers = [...this.#disposers];
    this.#disposers.clear();
    const errors: unknown[] = [];
    for (const dispose of disposers) {
      try {
        dispose();
      } catch (error) {
        errors.push(error);
      }
    }
    if (errors.length > 0) throw new AggregateError(errors, "one or more resource disposers failed");
  }

  get size(): number {
    return this.#disposers.size;
  }
}
