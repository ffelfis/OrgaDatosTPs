import pandas as pd
import numpy as np

def cambio_tipos(x):
    # Columnas numéricas
    x['building_id'] = x['building_id'].astype('int32')
    x['geo_level_1_id'] = x['geo_level_1_id'].astype('int8')
    x['geo_level_2_id'] = x['geo_level_2_id'].astype('int16')
    x['geo_level_3_id'] = x['geo_level_3_id'].astype('int16')
    x['count_floors_pre_eq'] = x['count_floors_pre_eq'].astype('int8')
    x['age'] = x['age'].astype('int16')
    x['area_percentage'] = x['area_percentage'].astype('int8')
    x['height_percentage'] = x['height_percentage'].astype('int8')
    x['count_families'] = x['count_families'].astype('int8')
    # Columnas Booleanas
    x['has_superstructure_adobe_mud'] = x['has_superstructure_adobe_mud'].astype('bool')
    x['has_superstructure_mud_mortar_stone'] = x['has_superstructure_mud_mortar_stone'].astype('bool')
    x['has_superstructure_stone_flag'] = x['has_superstructure_stone_flag'].astype('bool')
    x['has_superstructure_cement_mortar_stone'] = x['has_superstructure_cement_mortar_stone'].astype('bool')
    x['has_superstructure_mud_mortar_brick'] = x['has_superstructure_mud_mortar_brick'].astype('bool')
    x['has_superstructure_cement_mortar_brick'] = x['has_superstructure_cement_mortar_brick'].astype('bool')
    x['has_superstructure_timber'] = x['has_superstructure_timber'].astype('bool')
    x['has_superstructure_bamboo'] = x['has_superstructure_bamboo'].astype('bool')
    x['has_superstructure_rc_non_engineered'] = x['has_superstructure_rc_non_engineered'].astype('bool')
    x['has_superstructure_rc_engineered'] = x['has_superstructure_rc_engineered'].astype('bool')
    x['has_superstructure_other'] = x['has_superstructure_other'].astype('bool')
    x['has_secondary_use'] = x['has_secondary_use'].astype('bool')
    x['has_secondary_use_agriculture'] = x['has_secondary_use_agriculture'].astype('bool')
    x['has_secondary_use_hotel'] = x['has_secondary_use_hotel'].astype('bool')
    x['has_secondary_use_rental'] = x['has_secondary_use_rental'].astype('bool')
    x['has_secondary_use_institution'] = x['has_secondary_use_institution'].astype('bool')
    x['has_secondary_use_school'] = x['has_secondary_use_school'].astype('bool')
    x['has_secondary_use_industry'] = x['has_secondary_use_industry'].astype('bool')
    x['has_secondary_use_health_post'] = x['has_secondary_use_health_post'].astype('bool')
    x['has_secondary_use_gov_office'] = x['has_secondary_use_gov_office'].astype('bool')
    x['has_secondary_use_use_police'] = x['has_secondary_use_use_police'].astype('bool')
    x['has_secondary_use_other'] = x['has_secondary_use_other'].astype('bool')
    return x