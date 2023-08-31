**/on_search**
- /message/catalog/bpp~1providers/0/items/0/descriptor/images must NOT have more than 3 items
- /message/catalog/bpp~1providers/0/items/1/descriptor/images must NOT have more than 3 items

**/init**
- /message/order/billing/address must have required property 'building'


**/on_init**
- /billing/address must have required property 'building'


**/confirm**
- /message/order/billing/address must have required property 'building'
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- /billing/address must have required property 'building'
- Discrepancies between the quote object /on_select and /on_confirm

**/update**
- /message/order/items/0/tags/ttl_approval must match format "duration"


