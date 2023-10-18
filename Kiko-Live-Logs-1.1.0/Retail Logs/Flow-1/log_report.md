**/init**
- /message/order/billing/address must have required property 'building'
- /message/order/fulfillments/0/end/location/address/building must NOT have fewer than 3 characters
- address.building should be more than 3 chars

**/on_init**
- /billing/address must have required property 'building'

**/confirm**
- /message/order/billing/address must have required property 'building'

**/on_confirm**
- /billing/address must have required property 'building'

**/on_status (Pending)**
- /billing/address must have required property 'building'

**/on_status (Order-picked-up)**
- /billing/address must have required property 'building'

**/on_status (Order-Delivered)**
- /billing/address must have required property 'building'

