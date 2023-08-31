**/search**
- /message/intent must have required property 'item'

**/on_search**
- context/timestamp difference between /on_search and /search should be smaller than 5 sec

**/on_select**
- Warning: Quoted Price in /on_select INR 520 does not match with the total price of items in /select INR 1070

**/init**
- City code mismatch in /search and /init

**/on_init**
- City code mismatch in search & on_init
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- City code mismatch in /search and /confirm
- address/door mismatches in /billing in /init and /confirm
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- City code mismatch in /search and /on_confirm
- context/timestamp difference between /on_confirm and /confirm should be smaller than 5 sec
- Discrepancies between the quote object /on_select and /on_confirm

**/cancel**
- City code mismatch in /select and /cancel

**/on_cancel**
- City code mismatch in /search and /on_cancel

