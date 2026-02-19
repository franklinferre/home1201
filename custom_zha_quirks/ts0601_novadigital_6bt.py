"""Tuya TS0601 6-button wall switch quirk for _TZE204_tdhnhhiy (NovaDigital)."""

from zigpy.quirks.v2 import EntityType
import zigpy.types as t
from zhaquirks.tuya.builder import TuyaQuirkBuilder


class PowerOnBehavior(t.enum8):
    """Power-on behavior after power loss."""

    Off = 0x00
    On = 0x01
    LastState = 0x02


class IndicatorMode(t.enum8):
    """LED indicator mode."""

    Off = 0x00
    Synchronized = 0x01
    Inverted = 0x02


(
    TuyaQuirkBuilder("_TZE204_tdhnhhiy", "TS0601")
    .tuya_switch(
        dp_id=1,
        attribute_name="on_off_1",
        entity_type=EntityType.STANDARD,
        translation_key="switch_1",
        fallback_name="Switch 1",
    )
    .tuya_switch(
        dp_id=2,
        attribute_name="on_off_2",
        entity_type=EntityType.STANDARD,
        translation_key="switch_2",
        fallback_name="Switch 2",
    )
    .tuya_switch(
        dp_id=3,
        attribute_name="on_off_3",
        entity_type=EntityType.STANDARD,
        translation_key="switch_3",
        fallback_name="Switch 3",
    )
    .tuya_switch(
        dp_id=4,
        attribute_name="on_off_4",
        entity_type=EntityType.STANDARD,
        translation_key="switch_4",
        fallback_name="Switch 4",
    )
    .tuya_switch(
        dp_id=5,
        attribute_name="on_off_5",
        entity_type=EntityType.STANDARD,
        translation_key="switch_5",
        fallback_name="Switch 5",
    )
    .tuya_switch(
        dp_id=6,
        attribute_name="on_off_6",
        entity_type=EntityType.STANDARD,
        translation_key="switch_6",
        fallback_name="Switch 6",
    )
    .tuya_enum(
        dp_id=14,
        attribute_name="power_on_behavior",
        enum_class=PowerOnBehavior,
        entity_type=EntityType.CONFIG,
        translation_key="power_on_behavior",
        fallback_name="Power On Behavior",
    )
    .tuya_enum(
        dp_id=15,
        attribute_name="indicator_mode",
        enum_class=IndicatorMode,
        entity_type=EntityType.CONFIG,
        translation_key="indicator_mode",
        fallback_name="LED Indicator Mode",
    )
    .skip_configuration()
    .add_to_registry()
)
