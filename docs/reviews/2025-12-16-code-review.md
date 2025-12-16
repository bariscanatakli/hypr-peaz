# Code review – 2025-12-16

Findings (ordered by impact):

- **Scroll state flag never set** (`hyprpeaz/src/modules/audio.py:523-555`): `with_min_height` is never flipped to `True`/`False`, so once the list exceeds five items the scrollbar style can’t be restored when it shrinks. Set the flag when toggling to keep the min-height/scrollbar state in sync with the current item count.
- **Duplicate handlers and double cleanup** (`hyprpeaz/src/modules/audio.py:320-425`): `toggle_mute_and_close` is defined twice and `destroy()` disconnects the gesture twice/removes the controller twice. Consolidate the method and do single disconnect/removal to avoid future warnings or missed cleanup when more logic is added.
- **Type alias is just a string** (`hyprpeaz/src/modules/audio.py:12`): `type NodeItem = "EndpointItem | StreamItem"` stores a string instead of a real union, so it gives no type-safety and confuses readers. Use a proper alias (e.g., `from __future__ import annotations` + `NodeItem: TypeAlias = EndpointItem | StreamItem`).
