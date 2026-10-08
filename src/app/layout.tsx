import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Marco Trotta",
  description: "The personal website of Marco Trotta.",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en" data-theme="light">
      <body>{children}</body>
    </html>
  );
}
