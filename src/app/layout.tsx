import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Marco Trotta",
  description: "The personal website of Marco Trotta.",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en" data-theme="light">
      <head>
        <link
          rel="preload"
          href="/fonts/marco-marker.woff?v=2.1"
          as="font"
          type="font/woff"
          crossOrigin="anonymous"
        />
      </head>
      <body>{children}</body>
    </html>
  );
}
