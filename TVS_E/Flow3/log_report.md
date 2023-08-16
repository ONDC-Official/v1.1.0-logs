**/on_search**
- context/timestamp difference between /on_search and /search should be smaller than 5 sec
- Either one of fixed (range) or split (frequency and times) timings should be provided in /bpp/providers[0]/locations[0]/time

**/init**
- value of address.name, address.building and address.locality should be unique

**/on_init**
- Quoted Price 27658 does not match with Net Breakup Price 27658.000000000004 in /on_init
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- address/door mismatches in /billing in /init and /confirm
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- address/door mismatches in /billing in /confirm and /on_confirm
- Discrepancies between the quote object /on_select and /on_confirm
- payment object mismatches in /confirm & /on_confirm

**/on_status (Pending)**
- /fulfillments/0/start/time pickup time should not be present until order is picked
- address/door, address/street mismatches in /billing in /confirm and /on_status_pending

**/on_status (Order-picked-up)**
- address/door, address/street mismatches in /billing in /confirm and /on_status_picked

**/on_status (Order-Delivered)**
- address/door, address/street mismatches in /billing in /confirm and /on_status_delivered

**/on_update (Initiated)**
- /fulfillments/0/end/location/address must have required property 'locality'
- quote price should not change for return state Return_Initiated

**/on_update (Rejected)**
- /fulfillments/0/end/location/address must have required property 'locality'
- quote price should not change for return state Return_Rejected

