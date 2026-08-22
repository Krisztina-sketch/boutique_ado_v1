# Boutique Ado

## Introduction

Boutique Ado is an e-commerce website built with Django. The project allows users to browse products and view product details. “Products can be managed through the website by authorised users, as well as through the Django administration panel.”
This project was created as part of my Level 5 Web Application Development course.

## Features

- Responsive design for different screen sizes
- Product listing functionality
- Product detail pages
- Django admin panel for managing products
- Product images, descriptions and prices

## Technologies Used

- HTML5
- CSS3
- JavaScript
- Python
- Django
- SQLite database
- Git and GitHub

## Database

The project uses Django models to store product information.

The Product model contains:

- Product name
- Product description
- Product price
- Product image


## Products

Current products added:

- Straw Summer Hat
- Leather Handbag
- High Waist Denim Jeans
- Beige Summer Skirt
- Cream Knit Sweater
- Blue Casual Blouse
- Black Cocktail Dress
- White Evening Dress
- Floral Summer Dress
- Blue Summer Dress


## Image Credits

Product images were sourced from free image websites.

- Blue Summer Dress image:
  Elegant blue summer dress for a stylish and comfortable look.
  Source: Pexels
  Photographer: Александр Слесарев
  URL: https://www.pexels.com/photo/a-woman-wearing-a-blue-dress-15665840/
  
  White Evening Dress image:
  Classic white evening dress perfect for special occasions.
  Source: Pexels
  Photographer: Huy Nguyễn
  URL : https://www.pexels.com/photo/elegant-woman-in-white-dress-indoors-28673073/

  Floral Summer Dress image:
  Beautiful floral summer dress with a feminine style.
  Source: Pexels
  Photographer : Arthouse Studio
  URL : https://www.pexels.com/photo/woman-in-a-dress-and-a-hat-carrying-a-shopping-basket-4589211/

  Black Coctail Dress image :
  Elegant black cocktail dress for evening events.
  Source : Pexels
  Photographer :helin öner
  URL : https://www.pexels.com/photo/beautiful-woman-in-a-black-dress-on-a-wooden-door-frame-15006215/

  Cream Knit Sweater image :
  Soft knitted sweater for a cosy everyday outfit.
  Source : Pexels
  Photographer : Polina Tankilevitch
  URL :  https://www.pexels.com/photo/woman-in-white-knit-sweater-covering-her-face-with-her-sweater-6630847/

  Blue Casual Blouse image :
  Lightweight blouse for smart casual looks.
  Source : Pexels
  Potographer : Mâide Arslan
  URL : https://www.pexels.com/photo/young-woman-in-a-blue-shirt-against-a-stone-wall-20636650/

  High Waist Denim Jeans image :
  High Waist Denim Jeans
  Source :Pexels
  Photographer : Thirdman
  URL : https://www.pexels.com/photo/person-in-black-long-sleeve-shirt-with-hand-in-pocket-8053690/

  Beige Summer Skirt image:
  Lightweight skirt for warm weather.
  Source:Pexels
  Photographer:Patricia Bozan
  URL : https://www.pexels.com/photo/stylish-young-woman-standing-against-urban-wall-36625478/

  Straw Summer Hat image:
  Summer accessory to complete an outfit.
  Source:Pexels
  Photographer:hello aesthe
  URL: https://www.pexels.com/photo/close-up-of-a-hat-by-a-swimming-pool-25524555/

  Leather Handbag image:
  Elegant handbag for everyday use.
  Source:Pexels
  Photographer:Diana Light
  URL:https://www.pexels.com/photo/stylish-handbag-on-stool-in-light-room-4830924/

All images are used for educational purposes as part of this student project.

## Development Notes

Products are created and managed through the Django administration interface.

The administrator can add, edit and remove products without directly changing the database.

## Local Development

Clone this repository:

git clone [your GitHub link]

Install requirements:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

Start the server:

python manage.py runserver

## Credits

- Images: Pexels
- Framework: Django
- Programming language: Python
- Database: SQLite


## Testing

The website was tested throughout development to make sure the main features work correctly.

### Navigation

- Checked that the Home link works correctly.
- Checked that the Products link opens the product catalogue.
- Checked that the Add Product link opens the product management form for an authorised user.
- Checked that Sign In and Sign Out work correctly.

### Product Display

- Checked that products stored in the database appear on the Products page.
- Checked that product names, descriptions, prices and images display correctly.
- Checked that the View Product button opens the correct product detail page.
- Checked that products can be filtered using the category buttons.

### Product Management

The CRUD functionality was manually tested.

- **Create:** Added new products using the Add Product form and confirmed that they appeared on the Products page.
- **Read:** Checked that products can be viewed on the Products page and individual product detail pages.
- **Update:** Edited an existing product and confirmed that the updated information appeared correctly.
- **Delete:** Deleted a product and confirmed that it was removed from the product catalogue.

### Authentication

- Tested user sign in.
- Tested user sign out.
- Checked that navigation changes depending on whether the user is authenticated.
- Checked access to product management functionality.

### Django Admin

The Django administration panel was used to check and manage database records, users, email addresses, products and categories.

### Images

Product images were checked to make sure that they display correctly with the appropriate products.

### Responsive Design

The website was tested at different screen sizes to check that the layout remains usable and readable.
## Repository

GitHub: [boutique_ado_v1](https://github.com/Krisztina-sketch/boutique_ado_v1)

## User Authentication

The website includes user authentication using Django's built-in authentication system.

Users can:

- Create an account
- Sign in
- Sign out
- Access features according to their authentication status

Product management functionality is restricted so that unauthorised users cannot modify products.

## Product Management

Authorised users can manage products directly through the website.

The following CRUD functionality has been implemented:

- Create new products
- Read and view product information
- Update existing products
- Delete products

Product forms allow information such as the product name, description, price, category and image to be managed.

Confirmation is required before a product is deleted.

## Responsive Design

The website was designed to work across different screen sizes.

Bootstrap and custom CSS were used to create a responsive layout. The navigation, product catalogue and product detail pages adapt to different screen sizes.

## Known Issues

At the time of development, no major known issues prevent the core functionality of the website from working.

Further improvements could include:

- Improved product filtering and searching
- Additional user profile functionality
- Shopping basket and checkout functionality
- Improved image storage for production deployment

## Deployment

The project is prepared for deployment to Heroku.

Deployment requirements include:

- `requirements.txt` containing the Python dependencies
- `Procfile` containing the Gunicorn web process
- Gunicorn as the production web server

The Procfile contains:

`web: gunicorn boutique_ado.wsgi`

The final deployed application URL will be added here after deployment.

## Version Control

Git and GitHub were used for version control throughout development.

Changes were committed regularly during development and pushed to the GitHub repository.

Repository:

[boutique_ado_v1](https://github.com/Krisztina-sketch/boutique_ado_v1)

## Future Features

Possible future improvements include:

- Shopping basket functionality
- Online checkout and payments
- Product search
- Product filtering
- User profiles
- Product reviews
- Wishlist functionality
- Improved product image management
