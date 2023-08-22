**/on_select**
- Warning: Quoted Price in /on_select INR 67815 does not match with the total price of items in /select INR 82824

**/init**
- Warning: items[0].quantity.count for item ba3ca63c-927e-4ca3-8694-19e2c7b32911 mismatches with the items quantity selected in /select

**/on_init**
- Warning: items[0].quantity.count for item ba3ca63c-927e-4ca3-8694-19e2c7b32911 mismatches with the items quantity selected in /select
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- Warning: items[0].quantity.count for item ba3ca63c-927e-4ca3-8694-19e2c7b32911 mismatches with the items quantity selected in /select
- address/door mismatches in /billing in /init and /confirm
- Discrepancies between the quote object in /on_select and /confirm

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

