"use client";

import { useEffect, useState } from "react";

type Theme = "light" | "dark";

const socialLinks = [
  {
    label: "GitHub",
    href: "https://github.com/marco-trotta1",
    icon: (
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <path d="M12 .9a11.1 11.1 0 0 0-3.51 21.63c.56.1.76-.24.76-.54v-2.1c-3.1.67-3.76-1.32-3.76-1.32-.5-1.28-1.24-1.62-1.24-1.62-1.01-.69.08-.68.08-.68 1.12.08 1.71 1.15 1.71 1.15 1 1.7 2.61 1.21 3.24.92.1-.72.39-1.21.71-1.49-2.47-.28-5.06-1.24-5.06-5.5 0-1.22.44-2.21 1.15-2.99-.12-.28-.5-1.42.11-2.96 0 0 .94-.3 3.06 1.14a10.6 10.6 0 0 1 5.57 0c2.12-1.44 3.05-1.14 3.05-1.14.61 1.54.23 2.68.12 2.96.72.78 1.14 1.77 1.14 2.99 0 4.27-2.6 5.21-5.08 5.49.4.35.76 1.02.76 2.06v3.09c0 .3.2.65.77.54A11.1 11.1 0 0 0 12 .9Z" />
      </svg>
    ),
  },
  {
    label: "LinkedIn",
    href: "https://www.linkedin.com/in/marco-trotta-354030353",
    icon: (
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <path d="M20.45 2H3.55C2.69 2 2 2.68 2 3.52v16.96c0 .84.69 1.52 1.55 1.52h16.9c.86 0 1.55-.68 1.55-1.52V3.52c0-.84-.69-1.52-1.55-1.52ZM7.93 18.68H4.98V9.15h2.95v9.53ZM6.46 7.85a1.71 1.71 0 1 1 0-3.42 1.71 1.71 0 0 1 0 3.42Zm12.22 10.83h-2.95v-4.64c0-1.1-.02-2.51-1.53-2.51-1.54 0-1.78 1.2-1.78 2.43v4.72H9.47V9.15h2.83v1.3h.04c.39-.75 1.36-1.53 2.8-1.53 2.99 0 3.54 1.97 3.54 4.53v5.23Z" />
      </svg>
    ),
  },
  {
    label: "X",
    href: "https://x.com/marcotrotta_",
    icon: (
      <svg viewBox="0 0 24 24" aria-hidden="true">
        <path d="M18.9 2H22l-6.78 7.75L23.2 22h-6.25l-4.9-7.42L5.56 22H2.43l7.25-8.29L1.8 2h6.41l4.43 6.77L18.9 2Zm-1.1 18h1.73L7.27 3.89H5.42L17.8 20Z" />
      </svg>
    ),
  },
];

function applyTheme(theme: Theme) {
  document.documentElement.dataset.theme = theme;
  window.localStorage.setItem("marco-theme", theme);
}

export default function Home() {
  const [theme, setTheme] = useState<Theme>("light");

  useEffect(() => {
    const savedTheme = window.localStorage.getItem("marco-theme");
    const nextTheme: Theme = savedTheme === "dark" ? "dark" : "light";
    setTheme(nextTheme);
    document.documentElement.dataset.theme = nextTheme;
  }, []);

  function toggleTheme() {
    const nextTheme: Theme = theme === "light" ? "dark" : "light";
    setTheme(nextTheme);
    applyTheme(nextTheme);
  }

  return (
    <main className="site-shell">
      <header className="topbar">
        <button
          className="theme-toggle"
          type="button"
          role="switch"
          aria-checked={theme === "dark"}
          aria-label="Dark mode"
          onClick={toggleTheme}
        >
          <span className="toggle-track" aria-hidden="true">
            <span className="toggle-thumb" />
          </span>
          <span className="toggle-label">{theme === "dark" ? "Dark" : "Light"}</span>
        </button>

        <nav className="social-links" aria-label="Social links">
          {socialLinks.map(({ label, href, icon }) => (
            <a key={label} href={href} target="_blank" rel="noreferrer" aria-label={label}>
              {icon}
            </a>
          ))}
        </nav>
      </header>

      <div className="marquee-wrap">
        <section className="marquee" aria-labelledby="site-title">
          <h1 id="site-title" className="marquee-name">Marco Trotta</h1>
          <div className="marquee-contact">
            <span>Mail:</span>
            <a href="mailto:marcotrotta909@gmail.com">marcotrotta909@gmail.com</a>
          </div>
          <span className="marquee-screw screw-top-left" aria-hidden="true" />
          <span className="marquee-screw screw-top-right" aria-hidden="true" />
          <span className="marquee-screw screw-bottom-left" aria-hidden="true" />
          <span className="marquee-screw screw-bottom-right" aria-hidden="true" />
        </section>
      </div>

      <div className="open-sign" role="img" aria-label="Open">
        <svg viewBox="0 0 360 154" aria-hidden="true">
          <ellipse className="neon-blue" cx="180" cy="77" rx="150" ry="55" />
          <text className="neon-open" x="180" y="99" textAnchor="middle">OPEN</text>
        </svg>
      </div>

      <div className="sections">
        <section className="writing-section" id="about">
          <p className="section-index">01</p>
          <h2>About me / Interests</h2>
          <div className="writing-space" aria-hidden="true" />
        </section>

        <section className="writing-section" id="built">
          <p className="section-index">02</p>
          <h2>What I have built</h2>
          <div className="writing-space" aria-hidden="true" />
        </section>
      </div>

    </main>
  );
}
