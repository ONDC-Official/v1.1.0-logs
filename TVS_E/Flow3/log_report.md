**/on_search**
- /message/catalog/bpp~1providers/0/@ondc~1org~1fssai_license_no must NOT have fewer than 14 characters

**/init**
- value of address.name, address.building and address.locality should be unique

**/on_init**
- address.area_code in fulfillments[0].end.location mismatch in /select & /on_init

**/confirm**
- address/door mismatches in /billing in /init and /confirm
- fulfillments[0].end.location.address.area_code is not matching with area_code in /select

**/on_confirm**
- address/door mismatches in /billing in /confirm and /on_confirm
- Discrepancies between the quote object /on_select and /on_confirm
- payment object mismatches in /confirm & /on_confirm

**/on_status (Pending)**
- address/door mismatches in /billing in /confirm and /on_status_pending

**/on_status (Order-picked-up)**
- address/door mismatches in /billing in /confirm and /on_status_picked

**/on_status (Order-Delivered)**
- address/door mismatches in /billing in /confirm and /on_status_delivered

