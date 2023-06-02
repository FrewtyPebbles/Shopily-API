# Shopily API

An API for a mock e-commerce website made using Fastapi and MongoDB.

## Endpoints

### /item

This endpoint is used to add, remove, and update items.

 - `post` : Used to create/add new items. Takes in form data with the following parameters:

	 - `name` : Name of the product.

	 - `alt_names` : A json list of alternative names for the product.

	 - `description` : A long description of the item.

	 - `short_description` : A short description of the item.

	 - `sellers` : A json list of the sellers/companies that produce the item.

	 - `price` : A float representing the price of the item.

	 - `rating` : A float representing the rating of the item.

	 - `tags` : A json list of relevant search tags of the item.

	 - `types` : A json list of types/categories the item falls under.

	 - `main_img` : An image file that will be the main image displayed for the item.

	 - `alt_imgs` : One or more image files that will act as backup/complimentary images for the item.

