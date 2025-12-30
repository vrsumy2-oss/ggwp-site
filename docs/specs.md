# Functional Specifications: GGWP-Site

## 1. Project Overview
A peer-to-peer (P2P) marketplace for gamers to buy and sell in-game assets (Currency, Accounts, Skins, Boosting services). The platform acts as a middleman (escrow) to ensure safety.

## 2. User Roles
*   **Guest**: Can browse items, view prices, read guides.
*   **User (Authenticated)**:
    *   **Buyer**: Can top up wallet, chat with sellers, purchase items, leave reviews.
    *   **Seller**: Can post items, manage inventory, withdraw funds (simulated), chat with buyers.
*   **Admin**: Can manage users, ban accounts, resolve disputes, manage game categories.

## 3. Core Features & User Flows

### 3.1 Authentication & Profile
*   **Register/Login**: Email & Password.
*   **Profile**: Avatar, Display Name, Bio.
*   **Wallet**:
    *   `Balance`: Current available funds.
    *   `Frozen`: Funds held during an active transaction.
    *   **Flow**: User clicks "Top Up" -> (Mock Payment) -> Balance increases.

### 3.2 Marketplace Structure
*   **Games**: Top level grouping (e.g., "World of Warcraft", "CS2").
*   **Categories**: Sub-grouping (e.g., "Gold", "Accounts", "Items").
*   **Listings (Items)**:
    *   Title, Description, Price.
    *   Stock (amount available).
    *   Delivery Time (e.g., "Instant", "1 hour").
    *   Images (Screenshots).

### 3.3 Purchasing Flow (The "Escrow" Model)
1.  **Order Creation**: Buyer clicks "Buy". Balance is moved to `Frozen`. Order status: `PENDING`.
2.  **Process**: Seller is notified. Seller delivers item in-game.
3.  **Delivery**: Seller clicks "Delivered" on site. Order status: `DELIVERED`.
4.  **Confirmation**: Buyer verifies receipt in-game and clicks "Confirm" on site.
    *   *Auto-confirm timer:* If buyer doesn't react in 24h, auto-confirm.
5.  **Completion**: `Frozen` funds moved to Seller's `Balance`. Order status: `COMPLETED`.
6.  **Dispute (Edge Case)**: If Buyer claims non-delivery, Order status: `DISPUTE`. Admin intervenes.

### 3.4 Payment Integration (New)
*   **Gateway**: Stripe (Sandbox Mode) or PayPal (Sandbox).
*   **Top-Up Flow**:
    1.  User selects amount (e.g., $10).
    2.  Redirected to Stripe Checkout (Hosted Page).
    3.  Enters "Test Card" details (provided by Stripe).
    4.  Success -> Redirect back to site -> Webhook updates User Balance.
    5.  Failure -> Show error message.

### 3.5 Feedback System
*   After `COMPLETED` order, Buyer rates Seller (1-5 stars) and leaves a comment.
*   Seller's overall rating is displayed on their listings.

## 4. Admin Panel Features
*   **User Management**: List users, see balances.
*   **Order Management**: View all orders, ability to force-complete or refund disputed orders.
*   **Game Configuration**: Add new games or categories dynamically without changing code.

## 5. Technical Requirements
*   **Frontend**: HTML/CSS/JS (vanilla or lightweight framework). Focus on "Premium Gaming" aesthetic (Dark mode, neon accents).
*   **Backend**: Django + Django REST Framework.
*   **Database**: PostgreSQL.
*   **API**: RESTful JSON API.
