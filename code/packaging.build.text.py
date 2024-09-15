package = []
packaging_data = ('20 pieces in 1 pack / 10 packs in 1 carton / 4 cartons in 1 box')

'''for data in packaging_data.split('/'):
    m_item = data.split(" in ")[0]
    m_quantity = int(m_item.split()[0])
    m_item = m_item.split()[1].strip()
    package.append({m_item: m_quantity})
    s_item = data.split(" in ")[1]
    s_quantity = int(s_item.split()[0])
    s_item = s_item.split()[1].strip()
    package.append({s_item: s_quantity})

for data in packaging_data.split(' / '):
        m_item = data.split(" in ")[0]
        m_quantity = int(m_item.split()[0])
        m_item = m_item.split()[1].strip()
        package.append({m_item: m_quantity})
        
        s_item = data.split(" in ")[1]
        s_quantity = int(s_item.split()[0])
        s_item = s_item.split()[1].strip()
        
        # Check if the container is already included in the list
        if not any(s_item in d for d in package):
            package.append({s_item: s_quantity})
            
for data in packaging_data.split('/'):
    item = data.split(" in ")[0]
    quantity = int(item.split()[0])
    item = item.split()[1].strip()
    package.append({item: quantity})
    
    # get the last one
    item = data.split(" in ")[-1]
    quantity = int(item.split()[0])
    item = item.split()[1].strip()
    package.append({item: quantity})
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

for i in range(len(temp_package) - 1):
        current_item = list(temp_package[i].keys())[0].rstrip('s')
        next_item = list(temp_package[i + 1].keys())[0].rstrip('s')
        if current_item != next_item:
            package.append(temp_package[i])
package.append(temp_package[-1])
print(package)