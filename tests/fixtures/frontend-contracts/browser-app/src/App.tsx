import { useEffect, useRef, useState } from "react";
import { classifyMediaCapability, safeNavigationUrl, type MediaCapability } from "./browser-contract";

export function App(): React.JSX.Element {
  const [view, setView] = useState<"home" | "details">("home");
  const [capability, setCapability] = useState<MediaCapability>("indeterminate");
  const detailsHeading = useRef<HTMLHeadingElement>(null);
  const safeHelp = safeNavigationUrl("/help");

  useEffect(() => {
    if (view === "details") detailsHeading.current?.focus();
  }, [view]);

  function showDetails(): void {
    setView("details");
  }

  async function checkCapability(): Promise<void> {
    setCapability(await classifyMediaCapability(navigator, window.isSecureContext));
  }

  return (
    <main>
      <header className="hero">
        <p className="eyebrow">Portable frontend contract</p>
        <h1>Browser behavior with explicit boundaries</h1>
      </header>

      <section className="card-shell" aria-labelledby="fixture-heading">
        {view === "home" ? (
          <>
            <h2 id="fixture-heading">Representative flow</h2>
            <p>The fixture proves navigation focus, reflow, runtime validation, and capability fallbacks.</p>
            <button type="button" onClick={showDetails}>Open details</button>
          </>
        ) : (
          <>
            <h2 id="fixture-heading" ref={detailsHeading} tabIndex={-1}>Details ready</h2>
            <p>Focus moved with the view so keyboard and assistive-technology users receive context.</p>
            <button type="button" onClick={() => setView("home")}>Back</button>
          </>
        )}
      </section>

      <section aria-labelledby="capability-heading">
        <h2 id="capability-heading">Runtime capability</h2>
        <p id="capability-status" role="status">Camera capability: {capability}</p>
        <button type="button" aria-describedby="capability-status" onClick={() => void checkCapability()}>
          Check camera capability
        </button>
      </section>

      {safeHelp ? <a href={safeHelp.pathname}>Help</a> : null}
    </main>
  );
}
