#!/usr/bin/env python3
import toml

plan_widths = {
    "Condensed": {
        "shape": 500,
        "menu": 5,
        "css": "normal",
    },
    "Expanded": {
        "shape": 550,
        "menu": 5,
        "css": "normal",
    }
}

weights = {
    "Thin":       100,
    "ExtraLight": 200,
    "Light":      300,
    "Regular":    400,
    "Medium":     500,
    "SemiBold":   600,
    "Bold":       700,
}

weights_expanded = {
    weight_name: {"shape": weight_value, "menu": weight_value, "css": weight_value}
    for weight_name, weight_value in weights.items()
}

base_config = toml.load('base.toml')
base_plan = base_config['buildPlans']['Iosevka']
base_plan['weights'] = weights_expanded

for plan_name, shape in plan_widths.items():
    new_plan = dict(**base_plan)
    family_name = f"{new_plan['family']}{plan_name}"
    new_plan['family'] = family_name
    new_plan['widths'] = {"Normal": shape}
    base_config['buildPlans'][family_name] = new_plan

with open('private-build-plans.toml', 'w') as fd:
    toml.dump(base_config, fd)
