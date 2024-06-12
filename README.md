# Ice Cream Parlor Cafe Application

Welcome to the Ice Cream Parlor Cafe Application! This is a simple Python application designed to manage the operations of a fictional ice cream parlor cafe. It uses SQLite to handle the following tasks:

- Managing seasonal flavor offerings
- Tracking ingredient inventory
- Handling customer flavor suggestions and allergy concerns

## Features

### For Users
- **Maintain a Cart**: Users can maintain a cart of their favorite products.
- **Search & Filter Offerings**: Users can search and filter the available seasonal flavors based on their preferences.
- **Add Allergens**: Users can add new allergens to the database if they don’t already exist.

## Requirements

- Python 3.x
- SQLite

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Johnraj13/Python_App.git
   cd Python_App
   ```

2. Install the required Python packages:

   ```sh
   pip install -r requirements.txt
   ```

3. Initialize the SQLite database:

   ```sh
   python initialize_db.py
   ```

## Usage

1. Run the application:

   ```sh
   python app.py
   ```

2. Follow the on-screen instructions to interact with the application.

### Maintaining a Cart

- Add products to your cart by selecting them from the list of offerings.
- View and manage the items in your cart.

### Searching & Filtering Offerings

- Use the search function to find specific flavors.
- Apply filters to narrow down the list of available flavors based on your preferences.

### Adding Allergens

- If an allergen does not exist in the database, you can add it through the application's interface.

## Database Schema

### Tables

- `seasonal_flavors`: Stores information about seasonal flavor offerings.
- `ingredients`: Tracks ingredient inventory.
- `customer_suggestions`: Handles customer flavor suggestions and allergy concerns.
- `allergens`: Contains a list of allergens.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Push your branch and create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please contact johnraj.i2020@vitstudent.ac.in.

---

Enjoy managing your ice cream parlor with ease using this application!
