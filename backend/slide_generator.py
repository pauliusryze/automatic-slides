import pandas as pd
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from template_config import TEMPLATE_CONFIG

def set_font(paragraph, size, color, bold=False):
    paragraph.font.size = Pt(size)
    paragraph.font.bold = bold
    paragraph.font.color.rgb = color
    paragraph.font.name = 'Montserrat'


def generate_pptx_from_csv_and_images(csv_path, image_paths, output_path):
    df = pd.read_csv(csv_path, encoding='latin1')
    prs = Presentation()
    prs.slide_width = Inches(TEMPLATE_CONFIG['slide_width'])
    prs.slide_height = Inches(TEMPLATE_CONFIG['slide_height'])
    
    for index, row in df.iterrows():
        slide_layout = prs.slide_layouts[6]
        slide = prs.slides.add_slide(slide_layout)

        for shape_config in TEMPLATE_CONFIG['shapes']:
            if shape_config['name'] == 'Title':
                title_box = slide.shapes.add_textbox(
                    Inches(shape_config['left']), 
                    Inches(shape_config['top']), 
                    Inches(shape_config['width']), 
                    Inches(shape_config['height'])
                )
                title_frame = title_box.text_frame
                title_frame.clear()
                p = title_frame.paragraphs[0]
                p.text = str(row['title'])
                set_font(p, shape_config['font_size'], RGBColor(153, 81, 44), bold=True)
                p.alignment = PP_ALIGN.LEFT
                
            elif shape_config['name'] == 'Main Image':
                if len(image_paths) >= 1 and os.path.exists(image_paths[0]):
                    slide.shapes.add_picture(
                        image_paths[0], 
                        Inches(shape_config['left']), 
                        Inches(shape_config['top']), 
                        Inches(shape_config['width']), 
                        Inches(shape_config['height'])
                    )
            elif shape_config['name'] == 'AA1 Label':
                aa1_box = slide.shapes.add_textbox(
                    Inches(shape_config['left']), 
                    Inches(shape_config['top']), 
                    Inches(shape_config['width']), 
                    Inches(shape_config['height'])
                )
                aa1_frame = aa1_box.text_frame
                aa1_frame.clear()
                p = aa1_frame.paragraphs[0]
                p.text = "AA1"
                set_font(p, shape_config['font_size'], RGBColor(0, 0, 0), bold=True)
                p.alignment = PP_ALIGN.LEFT
            elif shape_config['name'] == 'Metrics':
                metrics_box = slide.shapes.add_textbox(
                    Inches(shape_config['left']), 
                    Inches(shape_config['top']), 
                    Inches(shape_config['width']), 
                    Inches(shape_config['height'])
                )
                metrics_frame = metrics_box.text_frame
                metrics_frame.clear()
                metrics_lines = str(row['metrics_raw']).split('|')
                for i, line in enumerate(metrics_lines):
                    p = metrics_frame.add_paragraph() if i > 0 else metrics_frame.paragraphs[0]
                    p.text = line.strip()
                    color = RGBColor(0, 0, 0)
                    if 'Spend' in line or 'CAC' in line:
                        color = RGBColor(153, 81, 44)
                    elif 'New Visits' in line or 'ECR' in line:
                        color = RGBColor(34, 139, 34)
                    set_font(p, shape_config['font_size'], color)
                    p.alignment = PP_ALIGN.LEFT
                    p.level = 0
                    p.bullet = True
            elif shape_config['name'] == 'Notes':
                notes_box = slide.shapes.add_textbox(
                    Inches(shape_config['left']), 
                    Inches(shape_config['top']), 
                    Inches(shape_config['width']), 
                    Inches(shape_config['height'])
                )
                notes_frame = notes_box.text_frame
                notes_frame.clear()
                # Embed FB and IG links as hyperlinks if present
                fb_text = str(row.get('fb_link_text', 'FB Link'))
                fb_url = str(row.get('fb_link_url', ''))
                ig_text = str(row.get('ig_link_text', 'IG Link'))
                ig_url = str(row.get('ig_link_url', ''))
                p = notes_frame.paragraphs[0]
                p.clear()
                if fb_url:
                    run = p.add_run()
                    run.text = fb_text
                    run.hyperlink.address = fb_url
                    run.font.bold = True
                    run.font.color.rgb = RGBColor(32, 102, 148)
                else:
                    run = p.add_run()
                    run.text = fb_text
                    run.font.bold = True
                    run.font.color.rgb = RGBColor(32, 102, 148)
                p.add_run().text = ' | '
                if ig_url:
                    run = p.add_run()
                    run.text = ig_text
                    run.hyperlink.address = ig_url
                    run.font.bold = True
                    run.font.color.rgb = RGBColor(32, 102, 148)
                else:
                    run = p.add_run()
                    run.text = ig_text
                    run.font.bold = True
                    run.font.color.rgb = RGBColor(32, 102, 148)
                p.alignment = PP_ALIGN.LEFT
            elif shape_config['name'] == 'Bottom Image 1':
                if len(image_paths) >= 2 and os.path.exists(image_paths[1]):
                    slide.shapes.add_picture(
                        image_paths[1], 
                        Inches(shape_config['left']), 
                        Inches(shape_config['top']), 
                        Inches(shape_config['width']), 
                        Inches(shape_config['height'])
                    )
            elif shape_config['name'] == 'Bottom Image 2':
                if len(image_paths) >= 3 and os.path.exists(image_paths[2]):
                    slide.shapes.add_picture(
                        image_paths[2], 
                        Inches(shape_config['left']), 
                        Inches(shape_config['top']), 
                        Inches(shape_config['width']), 
                        Inches(shape_config['height'])
                    )
    prs.save(output_path)
    return output_path
