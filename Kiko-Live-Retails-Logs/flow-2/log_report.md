**/search**
- /message/intent must have required property 'item'

**/on_search**
- store enable/disable timestamp (/bpp/providers/time/timestamp) must match context.timestamp

**/on_select**
- Warning: Quoted Price in /on_select INR 147.5 does not match with the total price of items in /select INR 150

**/init**
- /message/order/billing/address must have required property 'building'
- /message/order/fulfillments/0/end/location/address/building must NOT have fewer than 3 characters
- City code mismatch in /search and /init
- address.building should be more than 3 chars

**/on_init**
- /billing/address must have required property 'building'
- City code mismatch in search & on_init
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- /message/order/billing/address must have required property 'building'
- City code mismatch in /search and /confirm
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- /billing/address must have required property 'building'
- City code mismatch in /search and /on_confirm
- Discrepancies between the quote object /on_select and /on_confirm

**/cancel**
- City code mismatch in /select and /cancel
- Message Id cannot be same for different sets of APIs
- Cancellation reason id is not a valid reason id (buyer app initiated)

**/on_cancel**
- City code mismatch in /search and /on_cancel
- Cancellation Reason Id in /cancel and /on_cancel should be same

