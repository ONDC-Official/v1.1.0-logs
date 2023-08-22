**/init**
- /message/order/billing/address must have required property 'building'
- /message/order/fulfillments/0/end/location/address/building must NOT have fewer than 3 characters
- address.building should be more than 3 chars

**/on_init**
- /billing/address must have required property 'building'
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- /message/order/billing/address must have required property 'building'
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- /billing/address must have required property 'building'
- Discrepancies between the quote object /on_select and /on_confirm

**/on_status (Pending)**
- /billing/address must have required property 'building'

**/on_status (Order-picked-up)**
- /billing/address must have required property 'building'

**/on_status (Order-Delivered)**
- /billing/address must have required property 'building'

