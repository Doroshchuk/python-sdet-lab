from dataclasses import dataclass

from playwright.sync_api import Locator


@dataclass(frozen=True)
class ValidityState:
    bad_input: bool = False
    custom_error: bool = False
    pattern_mismatch: bool = False
    range_overflow: bool = False
    range_underflow: bool = False
    step_mismatch: bool = False
    too_long: bool = False
    too_short: bool = False
    type_mismatch: bool = False
    valid: bool = True
    value_missing: bool = False


def get_validity_state(locator: Locator) -> ValidityState:
    validity = locator.evaluate("""el => ({
        badInput: el.validity.badInput,
        customError: el.validity.customError,
        patternMismatch: el.validity.patternMismatch,
        rangeOverflow: el.validity.rangeOverflow,
        rangeUnderflow: el.validity.rangeUnderflow,
        stepMismatch: el.validity.stepMismatch,
        tooLong: el.validity.tooLong,
        tooShort: el.validity.tooShort,
        typeMismatch: el.validity.typeMismatch,
        valid: el.validity.valid,
        valueMissing: el.validity.valueMissing
    })""")

    return ValidityState(
        bad_input=validity["badInput"],
        custom_error=validity["customError"],
        pattern_mismatch=validity["patternMissmatch"],
        range_overflow=validity["rangeOverflow"],
        range_underflow=validity["rangeUnderflow"],
        step_mismatch=validity["stepMismatch"],
        too_long=validity["tooLong"],
        too_short=validity["tooShort"],
        type_mismatch=validity["typeMismatch"],
        valid=validity["valid"],
        value_missing=validity["valueMissing"],
    )
