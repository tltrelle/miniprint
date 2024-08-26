# ZPL generation code
def generate_zpl(printer_id, batch, item_code, description_line1, description_line2, manufacturer, manufacturer_part_line1, manufacturer_part_line2, warehouse, parent_warehouse, msl, qty, date, user):
    
    # Check if msl is a single digit or double digit and adjust the box size accordingly
    if len(msl) == 2:
        box = "^FO280,280^GB130,68,5,B,0^FS"
    else:
        box = "^FO280,280^GB110,68,5,B,0^FS"
    
    # Shorten warehouse name for Incoming Goods
    if warehouse == 'Incoming Goods':
        warehouse = 'Incoming'

    # Shorten parent warehouse name for All Warehouses and Kommissioniert
    if parent_warehouse == 'All Warehouses':
        parent_warehouse = 'All WH'
    elif (parent_warehouse == 'Kommissioniert-RO' or parent_warehouse == 'Kommissioniert-DE'):
        parent_warehouse = 'Kommissioniert'
    
    # Check if warehouse is long and adjust the font size accordingly
    if len(warehouse) > 7:
        warehouse = f"^CF0,30^FO280,200^FD{warehouse}^FS"
        parent_warehouse_yposition = '230'
    else:
        warehouse = f"^CF0,40^FO280,200^FD{warehouse}^FS"
        parent_warehouse_yposition = '240'
    
    # Check if parent warehouse is long and adjust the font size accordingly
    if len(parent_warehouse) > 9:
        parent_warehouse = f"^CF0,20^FO280,{parent_warehouse_yposition}^FD{parent_warehouse}^FS"
    else:
        parent_warehouse = f"^CF0,30^FO280,{parent_warehouse_yposition}^FD{parent_warehouse}^FS"

    # Generate the ZPL string...
    return f"""
    ^XA

    ^FO280,10
    ^BQN,2,5,H
    ^FDMM,A{batch}^FS

    ^CF0,20
    ^FO20,20^FDBatch^FS
    ^CF0,60
    ^FO20,45^FD{batch}^FS

    ^CF0,20
    ^FO20,105^FDItem Code^FS
    ^CF0,40
    ^FO20,130^FD{item_code}^FS

    ^CF0,20
    ^FO20,175^FDDescription^FS
    ^CF0,20
    ^FO20,200^FD{description_line1}^FS
    ^FO20,220^FD{description_line2}^FS

    ^CF0,20
    ^FO20,250^FDManufacturer^FS
    ^CF0,20
    ^FO20,275^FD{manufacturer}^FS
    ^FO20,295^FD{manufacturer_part_line1}^FS
    ^FO20,315^FD{manufacturer_part_line2}^FS

    ^CF0,20
    ^FO280,175^FDIncoming^FS
    {warehouse}
    {parent_warehouse}

    ^CF0,30
    {box}
    ^FO295,300^FDMSL {msl}^FS

    ^CF0,20
    ^FO20,370^FDQty^FS
    ^CF0,20
    ^FO20,395^FD{qty}^FS

    ^CF0,20
    ^FO90,370^FDDate^FS
    ^CF0,20
    ^FO90,395^FD{date}^FS

    ^CF0,20
    ^FO210,370^FDUser^FS
    ^CF0,20
    ^FO210,395^FD{user}^FS

    ^XZ
    """

# ZPL generation code for MSL Sticker
def generate_msl_sticker(printer_id, msl, date, time):

    # Trim MSL value
    msl = msl.replace('MSL ', '')

    # Update the mounting time based on the MSL level
    if msl == '1':
        mounting_time = 'Unlimited'
    elif msl == '2':
        mounting_time = '1 year'
    elif msl == '2A':
        mounting_time = '4 weeks'
    elif msl == '3':
        mounting_time = '168 hours'
    elif msl == '4':
        mounting_time = '72 hours'
    elif msl == '5':
        mounting_time = '48 hours'
    elif msl == '5A':
        mounting_time = '24 hours'
    elif msl == '6':
        mounting_time = 'Bake before use'

    # Check if msl is a single digit or double digit and adjust the position accordingly
    if len(msl) == 2:
        msl_print = f"^CF0,80^FO295,30^FD{msl}^FS"
    else:
        msl_print = f"^CF0,80^FO315,30^FD{msl}^FS"

    # Generate the ZPL string...
    return f"""
    ^XA

    ^FX Bounding Box
    ^FO10,10^GB380,380,1,B,0^FS

    ^FX Text Moisture Sensitive Device
    ^CF0,15^FO25,30^FDMOISTURE^FS
    ^CF0,15^FO25,53^FDSENSITIVE^FS
    ^CF0,15^FO25,76^FDDEVICE^FS

    ^FX Large Text MSL
    ^CF0,80^FO115,30^FDMSL^FS

    ^FX Large Text MSL Number
    ^CF0,80^FO315,30^FD{msl_print}^FS

    ^FX Horizontal Line
    ^FO10,110^GB380,1,1^FS

    ^FX Text Bag Seal date
    ^CF0,20^FO25,125^FDBag Seal Date: {date}^FS
    ^CF0,20^FO270,125^FDTime: {time}^FS
    ^CF0,20^FO25,160^FDMounting after opening: {mounting_time}^FS
    ^CF0,20^FO25,195^FDEmployee Signature:^FS

    ^FX Horizontal Line
    ^FO10,230^GB380,1,1^FS

    ^FX Text Bag Open date
    ^CF0,20^FO25,245^FDBag Open Date:^FS
    ^CF0,20^FO270,245^FDTime:^FS

    ^FX Text Expiration Date
    ^CF0,20^FO25,280^FDExpiration Date:^FS
    ^CF0,20^FO270,280^FDTime:^FS
    ^CF0,20^FO25,315^FDEmployee Signature:^FS

    ^FX Text Bottom
    ^CF0,18^FO25,363^FDMSL level defined by IPC/JEDEC J-STD-020^FS

    ^FX Black Box Negative
    ^LRY
    ^FO280,11
    ^GB109,99,95^FS

    ^FX Black Box Negative
    ^LRY
    ^FO11,350
    ^GB378,39,20^FS

    ^XZ
    """


# ZPL generation code for Special Instructions
def generate_special_instructions_label(printer_id, line_1, line_2, line_3, line_4, line_5, line_6, line_7, line_8, line_9, line_10, line_11, line_12):
    return f"""
    ^XA

    ^FX Bounding Box
    ^FO10,10^GB380,380,1,B,0^FS

    ^FX Special Instructions Header
    ^CF0,40, 45
    ^FO23,25^FDSpecial Instructions^FS

    ^FX Special Instructions Text
    ^CF0,25^FO25,90^FD{line_1}^FS
    ^CF0,25^FO25,115^FD{line_2}^FS
    ^CF0,25^FO25,140^FD{line_3}^FS
    ^CF0,25^FO25,165^FD{line_4}^FS
    ^CF0,25^FO25,190^FD{line_5}^FS
    ^CF0,25^FO25,215^FD{line_6}^FS
    ^CF0,25^FO25,240^FD{line_7}^FS
    ^CF0,25^FO25,265^FD{line_8}^FS
    ^CF0,25^FO25,290^FD{line_9}^FS
    ^CF0,25^FO25,315^FD{line_10}^FS
    ^CF0,25^FO25,340^FD{line_11}^FS
    ^CF0,25^FO25,365^FD{line_12}^FS

    ^FX Black Box Negative for Cell
    ^LRY
    ^FO11,11
    ^GB378,59,59^FS

    ^XZ
    """
