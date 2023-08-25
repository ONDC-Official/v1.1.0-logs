**/search**
- /message/intent must have required property 'item'

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

**/status**
- City code mismatch in /search and /status

**/on_status (Pending)**
- /billing/address must have required property 'building'
- /fulfillments/0/start must have required property 'time'
- /fulfillments/0/end must have required property 'time'
- City code mismatch in search and /on_status_pending

**/on_status (Order-picked-up)**
- /billing/address must have required property 'building'
- City code mismatch in search and /on_status_picked
- Timestamp for /on_confirm api cannot be greater than or equal to /on_status_picked api
- pickup timestamp should match context/timestamp and can't be future dated
- order/updated_at timestamp can't be less than the pickup time

**/on_status (Order-Delivered)**
- /billing/address must have required property 'building'
- City code mismatch in search and /on_status_delivered
- context/timestamp of /on_status_picked api cannot be greater than or equal to /on_status_delivered api
- delivery timestamp should match context/timestamp and can't be future dated
- order/updated_at timestamp can't be less than the delivery time

**/update**
- /message must have required property 'update_target'
- /message/order must have required property 'state'
- /message/order must have required property 'provider'
- /message/order must have required property 'items'
- City code mismatch in /search and /update
- Timestamp for /on_confirm api cannot be greater than or equal to /update api
- Message Id cannot be same for different sets of APIs

**/on_update (Initiated)**
- City code mismatch in /search and /on_update_Return_Initiated
- message_id of all unsolicited /on_update calls should be same for a particular /update request

**/on_update (Rejected)**
- City code mismatch in /search and /on_update_Return_Rejected

