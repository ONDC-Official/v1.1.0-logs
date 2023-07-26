**/on_search**
- Either one of fixed (range) or split (frequency and times) timings should be provided in /bpp/providers[0]/locations[0]/time

**/on_select**
- Warning: Quoted Price in /on_select INR 27608.000000000004 does not match with the total price of items in /select INR 27608

**/on_init**
- Quoted Price 27658 does not match with Net Breakup Price 27658.000000000004 in /on_init
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- address/door mismatches in /billing in /init and /confirm
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- address/door, created_at, updated_at mismatches in /billing in /confirm and /on_confirm
- Discrepancies between the quote object /on_select and /on_confirm
- payment object mismatches in /confirm & /on_confirm

**/on_status (Pending)**
- address/area_code, address/door, address/street mismatches in /billing in /confirm and /on_status_pending

**/on_status (Order-picked-up)**
- address/area_code, address/door, address/street mismatches in /billing in /confirm and /on_status_picked

**/on_status (Order-Delivered)**
- address/area_code, address/door, address/street mismatches in /billing in /confirm and /on_status_delivered

**/update**
- Message Id cannot be same for different sets of APIs

**/on_update (Initiated)**
- /fulfillments/0/end/location/address must have required property 'locality'
- quote price should not change for return state Return_Initiated
- delivery timestamp (/end/time/timestamp) can't change for fulfillment id 1

**/on_update (Return_Approved)**
- quote price should not change for return state Return_Approved
- delivery timestamp (/end/time/timestamp) can't change for fulfillment id 1

**/on_update (Return_Picked)**
- delivery timestamp (/end/time/timestamp) can't change for fulfillment id 1
- pickup timestamp should match context/timestamp and can't be future dated
- order/updated_at timestamp can't be less than the pickup time

**/on_update (Return_Delivered)**
- delivery timestamp (/end/time/timestamp) can't change for fulfillment id 1

