import sqlite3


def add_seasonal_flavor(name, ingredients, season):
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()
    c.execute('INSERT INTO seasonal_flavors (name, ingredients, season) VALUES (?, ?, ?)', (name, ingredients, season))
    conn.commit()
    conn.close()

def add_ingredient(name):
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()
    c.execute('INSERT INTO ingredients (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()

def add_customer_suggestion(flavor_name, suggested_by, allergens):
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()
    c.execute('INSERT INTO customer_suggestions (flavor_name, suggested_by, allergens) VALUES (?, ?, ?)', (flavor_name, suggested_by, allergens))
    conn.commit()
    conn.close()

def add_allergen(name):
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()
    c.execute('INSERT INTO allergens (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()

def add_to_cart(flavor_id):
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()
    c.execute('INSERT INTO cart (flavor_id) VALUES (?)', (flavor_id,))
    conn.commit()
    conn.close()

def search_flavors(keyword):
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()
    c.execute('SELECT * FROM seasonal_flavors WHERE name LIKE ?', ('%' + keyword + '%',))
    results = c.fetchall()
    conn.close()
    return results

def filter_flavors_by_season(season):
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()
    c.execute('SELECT * FROM seasonal_flavors WHERE season = ?', (season,))
    results = c.fetchall()
    conn.close()
    return results

# Function to check if an allergen already exists
def allergen_exists(name):
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()
    c.execute('SELECT * FROM allergens WHERE name = ?', (name,))
    result = c.fetchone()
    conn.close()
    return result is not None
