# Design System: Lara Pires Facial Aesthetics Landing Page
**Project ID:** projects/2535212709060853539

## 1. Visual Theme & Atmosphere
The design embodies a **Sophisticated Minimalism with Warmth**. It balances clinical precision with human elegance, creating a trustworthy and luxurious aesthetic suitable for high-end medical aesthetics. The vibe is "Serene," "Professional," and "Timeless," utilizing ample whitespace, fluid curves, and subtle interactions to convey care and quality.

## 2. Color Palette & Roles
* **Elegance Gold (Primary):** `#BCA578` - Used as the primary brand color for action buttons, key highlights, borders, and icons. Represents luxury and quality.
* **Deep Gold (Primary Dark):** `#A58F63` - Used for hover states of primary elements, adding depth to interactions.
* **Pure Clean Light (Background Light):** `#FAFAFA` - The main background color in light mode, providing a soft, sterile but not harsh canvas.
* **Dark Elegance (Background Dark):** `#1A1A1A` - The main background in dark mode, offering a premium, dramatic look.
* **Crisp Surface (Surface Light):** `#FFFFFF` - Used for cards and elevated sections in light mode to create subtle depth.
* **Dark Surface (Surface Dark):** `#262626` - Used for cards in dark mode.
* **Primary Text (Text Light):** `#333333` - High-contrast dark gray for ensuring readability on light backgrounds without the harshness of pure black.
* **Muted Text (Muted Light):** `#666666` - Used for supporting text and descriptions, softening the information density.

## 3. Typography Rules
* **Headings (Playfair Display):** A sophisticated serif font used for all major headings (H1-H4). It adds an editorial, high-fashion feel.
    *   **H1:** Very large (5xl-7xl), distinct, used for hero impact.
    *   **H2/H3:** Elegant, often paired with primary color accents.
* **Body (Montserrat):** A clean, geometric sans-serif used for navigation, body text, and buttons. It ensures legibility and modern simplicity.
    *   **Styles:** Often used with `uppercase` and `tracking-widest` for navigation links and buttons to create a premium feel.

## 4. Component Stylings
*   **Buttons:**
    *   **Primary:** Rectangular with standard rounding (`rounded`), uppercase text, gold background (`bg-primary`), and a subtle shadow (`shadow-lg`). Features a lift effect on hover (`-translate-y-0.5`).
    *   **Secondary/Link:** Simple text with an underline or bottom border, often uppercase and tracking-widest.
    *   **Navigation:** Clean text with hover color transition to Gold.
*   **Cards/Containers:**
    *   **Feature Cards:** Minimalist frames (`border border-gray-100`) with a subtle hover effect that highlights the border in Gold (`hover:border-primary/50`).
    *   **Image Cards:** Clean rounded corners (`rounded-lg`) with overflow hidden and deep shadows (`shadow-xl`) to lift them off the page.
*   **Imagery & Shapes:**
    *   **Organic Curves:** The hero section features a unique "leaf" or "petal" shape (`rounded-bl-[100px]`), breaking the grid and adding an organic, natural feel.
    *   **Icons:** Often enclosed in circular containers (`rounded-full`) with a light gold background (`bg-primary/10`).

## 5. Layout Principles
*   **Generous Spacing:** Sections are separated by large vertical padding (`py-20` or `py-24`), giving content room to breathe.
*   **Grid Structure:** Uses a standard 12-column logic (`max-w-7xl`, `grid-cols-12` or `grid-cols-3`), but often asymmetrical to create visual interest (e.g., text on one side, large image on the other).
*   **Layering:** Uses subtle background gradients (blur blobs) and absolute positioning to create depth without clutter.
