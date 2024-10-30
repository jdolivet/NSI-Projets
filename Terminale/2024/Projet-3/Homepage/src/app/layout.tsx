import type { Metadata } from "next";
import { Space_Mono } from "next/font/google";
import "@/styles/global.scss";
import Nav from "@/components/Nav";
import GLGradient from "@/components/GLGradient";

const spaceMono = Space_Mono({
  weight: ["400", "700"],
  style: "normal",
  subsets: ["latin"]
});

export const metadata: Metadata = {
  title: "zoe's website",
  description: "My personal website.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${spaceMono.className}`}>
        <Nav />
        <GLGradient />
        {children}
      </body>
    </html>
  );
}
