import wrds
import pandas as pd

print("="*60)
print("TAQ Access Test (Corrected)")
print("="*60)

db = wrds.Connection()

# Test 1: List tables in taqm_2023
print("\n1. Checking what's in taqm_2023...")
try:
    tables = db.list_tables(library='taqm_2023')
    print(f"✓ Found {len(tables)} tables in taqm_2023")
    print(f"Sample tables: {tables[:5]}")
except Exception as e:
    print(f"Error: {e}")

# Test 2: Try to access May 2023 trades
print("\n2. Testing AAPL trades for May 15, 2023...")
try:
    # Correct table format: ctm_YYYYMMDD in taqm_YYYY library
    query = """
    SELECT COUNT(*) as num_trades
    FROM taqm_2023.ctm_20230515
    WHERE sym_root = 'AAPL'
    """
    result = db.raw_sql(query)
    num_trades = result['num_trades'].iloc[0]
    print(f"✓ TAQ data works!")
    print(f"  AAPL had {num_trades:,} trades on 2023-05-15")
    
except Exception as e:
    print(f"Error: {e}")

# Test 3: Get sample data
print("\n3. Fetching sample AAPL trades...")
try:
    query = """
    SELECT 
        time_m as timestamp,
        sym_root as ticker,
        price,
        size
    FROM taqm_2023.ctm_20230515
    WHERE sym_root = 'AAPL'
    LIMIT 10
    """
    sample = db.raw_sql(query)
    print("✓ Sample data:")
    print(sample)
    
except Exception as e:
    print(f"Error: {e}")

db.close()
print("\n" + "="*60)
print("✓ TAQ access confirmed!")
print("="*60)
