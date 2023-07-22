**/on_search**
- /message/catalog/bpp~1providers/0/items/3/descriptor/images must NOT have more than 3 items
- /message/catalog/bpp~1providers/1/items/3/descriptor/images must NOT have more than 3 items
- /bpp/providers[1]/locations[0]/gps coordinates must be specified with at least six decimal places of precision.

**/on_select**
- tax line item should not be present if price=0
- Warning: Quoted Price in /on_select INR 400 does not match with the total price of items in /select INR 740

**/init**
- City code mismatch in /search and /init

**/on_init**
- City code mismatch in search & on_init
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- City code mismatch in /search and /confirm
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- City code mismatch in /search and /on_confirm
- Discrepancies between the quote object /on_select and /on_confirm

**/cancel**
- City code mismatch in /select and /cancel

**/on_cancel**
- City code mismatch in /search and /on_cancel

