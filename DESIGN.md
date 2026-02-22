# Design System

## Typography
- **Headings**: `Playfair Display` (Serif). Use `font-display` class.
- **Body**: `Montserrat` (Sans-serif). Use `font-body` class.

## Colors
- **Primary (Gold)**: `#D4AF37` (approx). Tailwind: `text-primary`, `bg-primary`.
- **Background Dark**: `#121212` (approx). Tailwind: `bg-surface-dark`.
- **Background Light**: `#F9F9F9`. Tailwind: `bg-surface-light`.
- **Text Light**: `#F3F4F6` (Gray 100).
- **Text Dark**: `#333333`.

## Components

### Hero Section
- **Height**: Full screen (`h-screen` or `min-h-[600px]`).
- **Background**: Image with dark overlay (`bg-black/50`).
- **Text**: Centered text, large serif heading ("FaceUp."), italic subtitle.
- **Buttons**:
    - Primary: Filled Gold (`bg-primary text-surface-dark`).
    - Secondary: Transparent with Border (`border border-white text-white`).

### Cards (Procedures)
- **Container**: `relative overflow-hidden group`.
- **Image**: High quality, `h-[500px]`, `object-cover`. Scale on hover.
- **Info Box**: White box overlay at bottom `-mt-12 mx-4 p-6 relative z-10 shadow-sm`.
- **Typography**: Serif Title (`text-lg`), Uppercase Category (`text-xs text-muted`).

### Section Headers
- **Layout**: Left aligned or centered.
- **Pre-title**: Uppercase, tracked (`tracking-[0.2em]`), Gold (`text-primary`).
- **Title**: Large Serif (`text-4xl`).

## Global Styles
- **Dark Mode**: Default for this luxury aesthetic.
- **Spacing**: Generous padding (`py-24`).
- **Icons**: Material Icons Outlined.
