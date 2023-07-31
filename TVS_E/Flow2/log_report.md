**/on_search**
- context/timestamp difference between /on_search and /search should be smaller than 5 sec
- category in serviceability construct should be one of the category ids bpp/providers[0]/items/category_id

**/on_init**
- Quoted Price 27658 does not match with Net Breakup Price 27658.000000000004 in /on_init
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- address/door mismatches in /billing in /init and /confirm
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- address/door mismatches in /billing in /confirm and /on_confirm
- Discrepancies between the quote object /on_select and /on_confirm
- payment object mismatches in /confirm & /on_confirm

