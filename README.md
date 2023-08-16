# QA_Store

This repository contains a Flask-based e-commerce web application designed for an online grocery store. Users can seamlessly browse and purchase a variety of items, manage their shopping carts, and place orders. The application is developed using the Flask web framework and leverages SQLAlchemy for database management.

## Technologies Used

The application was developed using a combination of the following technologies:

- **HTML:** Used for structuring the content and layout of web pages.
- **CSS:** Employed to style and enhance the visual presentation of the application.
- **Python:** The core programming language utilized for backend logic and server-side operations.
- **SQL:** Employed for database management and storage of essential application data.

## Features

- **Homepage:** The homepage showcases a curated selection of featured items and offers quick access to various store sections.

- **Shop:** Users can explore different item categories, delve into item specifics, and effortlessly add products to their shopping carts.

- **Shopping Cart:** Customers can review their cart contents, fine-tune item quantities, and effortlessly progress towards checkout.

- **Checkout:** Users can input their contact and shipping details, finalizing their purchase experience.

- **Orders:** Customers gain access to their historical orders and their current statuses.

- **Payment:** The application includes a payment simulation process, allowing users to input payment information to successfully complete their orders.

- **Item Categories:** Users have the option to peruse items grouped by categories such as fruits, vegetables, and dairy products.

- **Individual Item Pages:** Each product boasts a dedicated page brimming with comprehensive details.

## The application includes the following templates for various pages:

- `home.html`: Displays the homepage featuring featured items and store sections.
- `contact_us.html`: Renders the contact page for user inquiries.
- `about.html`: Provides information about the store and its mission.
- `shop.html`: Displays items available for purchase and supports adding items to the cart.
- `basket.html`: Displays the shopping cart contents and provides options for order placement.
- `checkout.html`: Allows users to input their contact and shipping information before finalizing orders.
- `orders.html`: Lists previous orders and their statuses.
- `payment.html`: Simulates the payment process for order completion.
- `categories.html`: Displays various item categories available for browsing.
- Template Files for Individual Items: A series of templates named after specific items (e.g., `apple.html`, `banana.html`) to showcase detailed information about each item.

# Models

The application's data management is facilitated through a set of models defined using SQLAlchemy, enabling seamless interaction with the underlying database. These models represent key entities within the e-commerce system.

## Types

The `Types` model acts as a classification system for items, enabling straightforward categorization. It includes the following fields:

- `id`: An auto-incremented integer serving as the primary key.
- `type`: A string field containing the name of the item category, such as "Fruits," "Vegetables," or "Dairy."

## Items

The `Items` model encapsulates individual products available for purchase. It encompasses attributes including:

- `id`: The primary key identifying the item.
- `name`: The name of the item.
- `stock`: The available quantity of the item.
- `price`: The price of the item.
- `type_id`: A foreign key linking to the relevant `Types` category.

## Basket

The `Basket` model represents a user's shopping cart, containing crucial details such as:

- `id`: The primary key assigned to the basket.
- `basket_status`: A string field indicating the status of the basket, either "Open" or "Closed."
- `created_time`: A timestamp indicating when the basket was created.
- `basket_items`: A one-to-many relationship connecting to the `BasketItem` model, encapsulating items within the basket.

The `Basket` model also features methods to calculate the total price of items within the basket and to list detailed item information per basket item.

## BasketItem

`BasketItem` associates items with specific baskets, featuring attributes like:

- `id`: The primary key assigned to the basket item.
- `basket_id`: A foreign key linking to the relevant `Basket` instance.
- `item_id`: A foreign key linking to the relevant `Items` instance.
- `quantity`: The quantity of the item in the basket.

This model includes properties to calculate the total price for items in the basket, fetch the item name, and retrieve the item price.

## Orders

The `Orders` model tracks completed orders, recording information such as:

- `id`: The primary key assigned to the order.
- `basket_id`: A foreign key linking to the corresponding `Basket`.
- `total_price`: The total price of the order.
- `created_time`: A timestamp indicating when the order was created.
- `order_status`: A string indicating the status of the order, either "Open" or "Closed."
- `full_name`: The customer's full name.
- `email`: The customer's email address.
- `address1`: The primary address of the customer.
- `address2`: An optional secondary address.
- `city`: The city of the customer.
- `post_code`: The postal code of the customer.

## Payment

The `Payment` model captures payment details for orders, with fields including:

- `id`: The primary key for the payment record.
- `order_id`: A foreign key linking to the corresponding `Orders` instance.
- `created_time`: A timestamp indicating when the payment record was created.
- `payment_status`: A string indicating the payment status, e.g., "Pending," "Paid."
- `full_name`: The customer's full name.
- `card_number`: The card number used for payment.
- `expiry_date`: The expiry date of the card.
- `cvv`: The CVV number of the card.

These models collaboratively manage and store data related to items, shopping carts, orders, and payments, forming the core functionality of the e-commerce application.

## Template

The templates for the Nature's Harvest Organics e-commerce website. The templates extends the `base.html` layout to make any for refactoring a lot easier.

## Project Planning with Jira

Throughout the development process of the Nature's Harvest Organics e-commerce web application, we utilized Jira for efficient project planning and management. Jira proved invaluable in organizing tasks, tracking progress, and ensuring timely completion of milestones. By creating user stories, assigning tasks, setting priorities, and monitoring the project's overall timeline, I was able to maintain a structured and organized development workflow. This comprehensive approach to project planning played a pivotal role in delivering a successful and feature-rich e-commerce platform.

## Deployment Automation with Jenkins

To ensure smooth and efficient build of the Nature's Harvest Organics e-commerce web application, I used Jenkins. Jenkins served as my automation tool for building the application to cloud environment.




