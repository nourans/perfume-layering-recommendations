"""logic for interpreting GPT output (i.e. domain-specific parsing)"""
from utils import save_perfumes, load_perfumes
from gpt_notes import get_layering_recs

def get_recs():
    gpt_output = get_layering_recs()
    output_list = gpt_output.split("Taste Analysis")
    return output_list[0]

def get_analysis():
    gpt_output = get_layering_recs()
    output_list = gpt_output.split("Taste Analysis")
    return output_list[1]