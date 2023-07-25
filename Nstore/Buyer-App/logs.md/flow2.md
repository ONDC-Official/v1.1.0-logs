**/on_search**
- /message/catalog/bpp~1providers/0/items/0/descriptor/images must NOT have fewer than 1 items
- /message/catalog/bpp~1providers/0/items/0/@ondc~1org~1statutory_reqs_packaged_commodities/manufacturer_or_packer_address must match pattern "^(?!\s*$).+"
- /message/catalog/bpp~1providers/0/items/0/descriptor/images must NOT have fewer than 1 items
- /message/catalog/bpp~1providers/0/items/1/descriptor/images must NOT have fewer than 1 items
- /message/catalog/bpp~1providers/0/items/1/@ondc~1org~1statutory_reqs_packaged_commodities/manufacturer_or_packer_address must match pattern "^(?!\s*$).+"
- /message/catalog/bpp~1providers/0/items/1/descriptor/images must NOT have fewer than 1 items
- /message/catalog/bpp~1providers/0/items/2/descriptor/images must NOT have fewer than 1 items
- /message/catalog/bpp~1providers/0/items/2/@ondc~1org~1statutory_reqs_packaged_commodities/manufacturer_or_packer_address must match pattern "^(?!\s*$).+"
- /message/catalog/bpp~1providers/0/items/2/descriptor/images must NOT have fewer than 1 items

**/on_select**
- tax line item should not be present if price=0

**/init**
- /message/order/fulfillments/0/end/location/address/name must NOT have fewer than 3 characters
- address.name should be more than 3 chars

**/on_cancel**
- cancellation_reason_id should be a valid cancellation id (unsolicited seller app initiated)

