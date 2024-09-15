'''
This is a module for parsing packging data
'''

def parse_packaging(packaging_data: str) -> list[dict]:
    '''
    This function parses a string of packaging data and returns a list of dictionaries.
    The order of the list implies the order of the packaging data.

    Examples:

    input: "12 eggs in 1 carton" 
    ouput: [{ 'eggs' : 12}, {'carton' : 1}]

    input: "6 bars in 1 pack / 12 packs in 1 carton"
    output: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]

    input: "20 pieces in 1 pack / 10 packs in 1 carton / 4 cartons in 1 box"
    output: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    '''

    temp_package = []

    for data in packaging_data.split(' / '):
        m_item = data.split(" in ")[0]
        m_quantity = int(m_item.split()[0])
        m_item = m_item.split()[1].strip()
        temp_package.append({m_item: m_quantity})
        
        s_item = data.split(" in ")[1]
        s_quantity = int(s_item.split()[0])
        s_item = s_item.split()[1].strip()
        temp_package.append({s_item: s_quantity})

    # Filter out consecutive duplicates
    #rstrip is used due to the plural form of items that is matching the strings
    package = []

    for i in range(len(temp_package) - 1):
        current_item = list(temp_package[i].keys())[0].rstrip('s')
        next_item = list(temp_package[i + 1].keys())[0].rstrip('s')
        if current_item != next_item:
            package.append(temp_package[i])
    package.append(temp_package[-1])
            
    return package
    


def calc_total_units(package: list[dict]) -> int:
    '''
    This function calculates the total number of items in a package

    Example:

    input: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]
    output 72 (e.g. 6*12*1)

    input: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    output: 800 (e.g. 20*10*4*1)
    '''
    num_list = []
    result = 1
    for value in package:
        num_list.append(list(value.values())[0])
    for num in num_list:
        result *= num
    return result


def get_unit(package: list[dict]) -> str:
    '''
    This function returns the items in the packaging (this is the first item in the list)

    Examples:

    input: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]
    output: bars

    input: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    output: pieces

    '''
    package_key = list(package[0].keys())[0]
    return package_key


# This will only run from here, not when imported
# # Use this for testing / debugging cases with the debugger
if __name__ == '__main__':
    
    text = "25 balls in 1 bucket / 4 buckets in 1 bin"
    package = parse_packaging(text)
    print(package)

    package_total = calc_total_units(package)
    unit = get_unit(package)
    print(f"{package_total} {unit} total")