#!/usr/bin/env python3
"""Generate call-for-papers.pdf for the FoDS workshop."""

from fpdf import FPDF
import os

BASE = r"C:\WORK\Manchester"

ORANGE   = (193, 75, 26)
ORANGE_M = (208, 96, 30)
GOLD_BR  = (212, 160, 32)
BROWN_DK = (26, 10, 2)
CREAM    = (251, 246, 238)
CREAM_DP = (242, 232, 213)
SAND     = (232, 213, 176)
TEXT     = (42, 21, 5)
TEXT_MID = (90, 58, 26)
WHITE    = (255, 255, 255)

LM, RM = 20, 20
CW = 170


class PDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        self.set_fill_color(*ORANGE)
        self.rect(0, 0, 210, 3, style='F')
        self.set_xy(LM, 6)
        self.set_font('Helvetica', 'I', 7.5)
        self.set_text_color(*TEXT_MID)
        self.cell(CW, 4,
            'Towards a Global South-driven Future for Development Studies — Call for Papers')
        self.set_draw_color(*SAND)
        self.line(LM, 12, 210 - RM, 12)
        self.set_y(16)

    def footer(self):
        self.set_y(-13)
        self.set_draw_color(*SAND)
        self.line(LM, self.get_y(), 210 - RM, self.get_y())
        self.set_xy(LM, self.get_y() + 2)
        self.set_font('Helvetica', 'I', 6.5)
        self.set_text_color(*TEXT_MID)
        self.cell(CW / 2, 4,
            'British Academy Writing Workshop Grant (IWW25/100268)', align='L')
        self.cell(CW / 2, 4, f'Page {self.page_no()}', align='R')


pdf = PDF('P', 'mm', 'A4')
pdf.set_margins(LM, LM, RM)
pdf.set_auto_page_break(True, margin=20)
pdf.add_page()

# ── Page 1 header ─────────────────────────────────────────────────────────────
pdf.set_fill_color(*ORANGE)
pdf.rect(0, 0, 210, 3, style='F')

HDR_H = 52
pdf.set_fill_color(*CREAM)
pdf.rect(0, 3, 210, HDR_H, style='F')

pdf.image(os.path.join(BASE, 'logo.png'), x=10, y=7, w=42)

pdf.set_xy(57, 10)
pdf.set_font('Helvetica', 'B', 16)
pdf.set_text_color(*BROWN_DK)
pdf.multi_cell(143, 7.5, 'Towards a Global South-driven\nFuture for Development Studies')

pdf.set_xy(57, 27)
pdf.set_font('Helvetica', 'B', 7.5)
pdf.set_text_color(184, 122, 10)
pdf.cell(143, 5, '1ST WORKSHOP IN INDONESIA  ·  TBC: APRIL 2027')

pdf.set_xy(57, 34)
pdf.set_fill_color(*CREAM_DP)
pdf.set_draw_color(*SAND)
pdf.rect(57, 34, 118, 6.5, style='FD')
pdf.set_xy(60, 35.3)
pdf.set_font('Helvetica', '', 7)
pdf.set_text_color(*TEXT_MID)
pdf.cell(112, 4, 'British Academy Writing Workshop Grant  ·  IWW25/100268')

# ── Kente band ────────────────────────────────────────────────────────────────
KY = 3 + HDR_H
kente = [BROWN_DK, ORANGE, GOLD_BR, ORANGE_M, BROWN_DK, GOLD_BR, ORANGE, BROWN_DK]
sw = 210 / len(kente)
for i, c in enumerate(kente):
    pdf.set_fill_color(*c)
    pdf.rect(i * sw, KY, sw + 0.3, 6, style='F')

# ── Institution logos strip ───────────────────────────────────────────────────
IY = KY + 6
IH = 26

pdf.set_fill_color(*WHITE)
pdf.rect(0, IY, 210, IH, style='F')

pdf.set_xy(0, IY + 2)
pdf.set_font('Helvetica', 'B', 5.5)
pdf.set_text_color(*TEXT_MID)
pdf.cell(210, 3.5, 'COLLABORATING INSTITUTIONS', align='C')

SLOT_W = 210 / 5
LOGO_Y = IY + 7
LOGO_H = 11

logos = [
    (os.path.join(BASE, 'images', 'logo-manchester.svg'), 'Manchester'),
    (os.path.join(BASE, 'images', 'logo-sdgcenter-unpad.png'), 'SDGs Center\nUnpad'),
    (os.path.join(BASE, 'images', 'logo-unisa-icon.png'), 'Univ. of\nSouth Africa'),
    (os.path.join(BASE, 'images', 'uj.png'), 'Univ. of\nJohannesburg'),
    (os.path.join(BASE, 'images', 'logo-kcl.png'), "King's College\nLondon"),
]

for i, (path, name) in enumerate(logos):
    sx = i * SLOT_W
    if os.path.exists(path):
        try:
            pdf.image(path, x=sx + 2, y=LOGO_Y, h=LOGO_H)
        except Exception:
            pdf.set_xy(sx, LOGO_Y + 2)
            pdf.set_font('Helvetica', 'B', 7)
            pdf.set_text_color(*ORANGE)
            pdf.cell(SLOT_W, 5, name.split('\n')[0], align='C')
    pdf.set_xy(sx, LOGO_Y + LOGO_H + 1.5)
    pdf.set_font('Helvetica', '', 5)
    pdf.set_text_color(*TEXT_MID)
    pdf.multi_cell(SLOT_W, 2.5, name, align='C')

pdf.set_draw_color(*SAND)
for i in range(1, 5):
    pdf.line(i * SLOT_W, IY + 5, i * SLOT_W, IY + IH - 2)

# ── Convenors strip ───────────────────────────────────────────────────────────
CY = IY + IH
CH = 16

pdf.set_fill_color(*CREAM_DP)
pdf.rect(0, CY, 210, CH, style='F')
pdf.set_fill_color(*ORANGE)
pdf.rect(0, CY, 210, 1.5, style='F')

pdf.set_xy(LM, CY + 3.5)
pdf.set_font('Helvetica', 'B', 6)
pdf.set_text_color(*ORANGE)
pdf.cell(CW, 3.5, 'CONVENORS', align='C')

pdf.set_xy(LM, CY + 8)
pdf.set_font('Helvetica', '', 7.5)
pdf.set_text_color(*TEXT_MID)
pdf.multi_cell(CW, 3.8,
    "Pritish Behuria (University of Manchester), Arief Anshory Yusuf (Padjadjaran University), "
    "Sebeka Plaatje (University of South Africa), Elvis Avenyo (University of Johannesburg) "
    "and Andy Sumner (King’s College London).",
    align='C')

pdf.set_y(CY + CH + 6)


# ── Helpers ───────────────────────────────────────────────────────────────────

def sec_head(title, dark=False):
    color = BROWN_DK if dark else ORANGE
    pdf.ln(2)
    y = pdf.get_y()
    pdf.set_fill_color(*color)
    pdf.rect(LM, y + 1.5, 4, 4, style='F')
    pdf.set_xy(LM + 7, y)
    pdf.set_font('Helvetica', 'B', 7.5)
    pdf.set_text_color(*color)
    pdf.cell(CW - 7, 5.5, title.upper())
    pdf.set_draw_color(*color)
    pdf.line(LM + 7, y + 5.5, LM + CW, y + 5.5)
    pdf.ln(5)


def body_text(text, size=9.5):
    pdf.set_font('Helvetica', '', size)
    pdf.set_text_color(*TEXT)
    pdf.multi_cell(CW, 4.8, text)
    pdf.ln(1.5)


def theme_card(title, text):
    cpl = 95
    card_h = (-(- len(title) // cpl)) * 5.5 + (-(- len(text) // cpl)) * 4.5 + 12
    if pdf.get_y() + card_h > 265:
        pdf.add_page()
    y0 = pdf.get_y()
    pdf.set_fill_color(*WHITE)
    pdf.set_draw_color(221, 208, 188)
    pdf.rect(LM, y0, CW, card_h, style='FD')
    pdf.set_fill_color(*ORANGE)
    pdf.rect(LM, y0, 2.5, card_h, style='F')
    pdf.set_xy(LM + 5, y0 + 3)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_text_color(*ORANGE)
    pdf.multi_cell(CW - 7, 5, title)
    pdf.set_x(LM + 5)
    pdf.set_font('Helvetica', '', 8.5)
    pdf.set_text_color(*TEXT)
    pdf.multi_cell(CW - 7, 4.3, text)
    pdf.set_y(max(pdf.get_y(), y0 + card_h) + 3)


def instr_box(text):
    cpl = 95
    box_h = (-(- len(text) // cpl)) * 4.8 + 12
    y0 = pdf.get_y()
    pdf.set_fill_color(*WHITE)
    pdf.set_draw_color(221, 208, 188)
    pdf.rect(LM, y0, CW, box_h, style='FD')
    pdf.set_xy(LM + 5, y0 + 5)
    pdf.set_font('Helvetica', '', 9)
    pdf.set_text_color(*TEXT)
    pdf.multi_cell(CW - 10, 4.8, text)
    pdf.set_y(max(pdf.get_y(), y0 + box_h) + 4)


def divider():
    pdf.ln(2)
    pdf.set_draw_color(*SAND)
    pdf.line(LM, pdf.get_y(), LM + CW, pdf.get_y())
    pdf.ln(6)


def info_card(title, text, x, w):
    y0 = pdf.get_y()
    cpl = max(1, int(w * 2.1))
    h = (-(- len(text) // cpl)) * 4.2 + 14
    pdf.set_fill_color(*CREAM_DP)
    pdf.set_draw_color(*SAND)
    pdf.rect(x, y0, w, h, style='FD')
    pdf.set_fill_color(*ORANGE)
    pdf.rect(x, y0, w, 2.5, style='F')
    pdf.set_xy(x + 3, y0 + 5)
    pdf.set_font('Helvetica', 'B', 7)
    pdf.set_text_color(*ORANGE)
    pdf.cell(w - 6, 4, title.upper())
    pdf.set_xy(x + 3, y0 + 10)
    pdf.set_font('Helvetica', '', 7.8)
    pdf.set_text_color(*TEXT)
    pdf.multi_cell(w - 6, 4, text)
    return h


def guidance_block(title, content_fn):
    if pdf.get_y() > 230:
        pdf.add_page()
    y0 = pdf.get_y()
    pdf.set_xy(LM + 5, y0 + 5)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_text_color(*BROWN_DK)
    pdf.cell(CW - 10, 5, title)
    pdf.set_draw_color(*SAND)
    pdf.line(LM + 5, y0 + 10, LM + CW - 5, y0 + 10)
    pdf.set_y(y0 + 13)
    content_fn()
    end_y = pdf.get_y() + 3
    pdf.set_draw_color(221, 208, 188)
    pdf.rect(LM, y0, CW, end_y - y0, style='D')
    pdf.set_y(end_y + 2)


# ── BACKGROUND ────────────────────────────────────────────────────────────────
sec_head("Background")
body_text(
    "Since its inception, development studies has appeared to be in perpetual crisis. "
    "The current geopolitical moment, as well as reductions in foreign aid, has contributed "
    "to these old discussions resurfacing. Despite what may seem to be uncertainty about the "
    "future of the field, new development studies programmes at undergraduate and postgraduate "
    "level have proliferated globally. There are also issues of consistent knowledge divides "
    "where the ‘Future of the Development Studies’ continues to be debated in North America "
    "and Europe yet the voices of the Global Majority, especially those residing in Asia and "
    "Africa remain hidden from sight."
)

sec_head("Workshops for Early-Career Researchers")
body_text(
    "To enhance spaces for early-career researchers based in the Global South, we will be "
    "holding two workshops on ‘Towards a Global South-driven Future for Development Studies’. "
    "The aim of the workshop is to centre the voices of early-career researchers working on "
    "‘development’ (broadly conceived) who are based in Asia and Africa. We see this as part "
    "of a series of events to deepen knowledge about the experiences of studying and researching "
    "development studies outside North America and Europe. The immediate goal of this programme "
    "(comprising one workshop in Indonesia and one in Johannesburg) is to publish one edited "
    "collection with a prestigious university press and/or a special issue, entirely comprising "
    "chapters written by early career scholars based in Asia and Africa.\n\n"
    "We invite extended abstracts (750–1,000 words) to be submitted by 30 September on one of "
    "the subjects listed below. These workshops are funded by a British Academy Writing Workshop "
    "grant (IWW25/100268), which was awarded in 2026, and is part of a collaboration between "
    "The University of Manchester, King’s College London, Padjadjaran University, University "
    "of South Africa and University of Johannesburg."
)

# ── THEMES ────────────────────────────────────────────────────────────────────
pdf.add_page()
sec_head("Call for Papers – Themes")

theme_card("1) Framing Development: Studying What?",
    "Defining development has always been contentious. The concept has been defined in so many "
    "ways and has become so laden with baggage that it now may act as a flashpoint for conflict "
    "between different schools of thought in development studies. For some, it means raising "
    "living standards — but even there, there is debate: targeting growth exclusively, focusing "
    "on structural transformation, or prioritising policies aimed at individual empowerment "
    "(through health and education). Others argue that development is associated with the "
    "imposition of western oppression in the form of modernity. Some call for socio-economic "
    "transformation or alternatives to development while others prefer a more minimalist status "
    "quo. There is also an overwhelming tendency to equate ‘development’ narrowly with "
    "‘foreign aid’, best epitomised by Adam Tooze’s recent claims of the ‘end of development’. "
    "However, development, to many in the Global South, has different origins and a very "
    "different meaning, not beholden to how Europeans and North Americans engage with the world."
)

theme_card("2) The Scope of Development: Studying Where?",
    "Development studies has always been specifically concerned with analysing socio-economic "
    "development in what are popularly considered ‘developing countries’. Binary categorisations "
    "of developing/developed, Global South/Global North have long been criticised by scholars "
    "from neighbouring disciplines. Structuralists made the case for distinguishing between "
    "‘core’ and ‘periphery’ on the basis of the subordinate position of ‘developing’ "
    "countries within the global political economy. Very few countries, most of which are in "
    "East Asia, have sustained economic transformation over the last 70 years. On the other "
    "hand, recent ‘global development’ scholarship has made the case for more universalist "
    "framings, arguing that differences between the Global South and North have blurred "
    "sufficiently to make the binary meaningless. Papers engaging with this theme should examine "
    "which regions ‘development studies’ should focus on and what the case should be for "
    "such a choice."
)

pdf.add_page()

theme_card("3) The Decolonisation of Knowledge: How to study ‘development’?",
    "Development studies has a prominent presence in Europe, attributed to colonial history. "
    "This version of development, associated with Harry Truman’s post-WWII speech, has been "
    "closely associated with aid-driven development and has been a target of criticism across "
    "the social sciences. Paradoxically, there are other Southern-based origin stories of "
    "development, most closely associated with Bandung, that are as notable. This history is "
    "influenced by an anti-imperialist agenda and the formal decolonisation process, emphasising "
    "emancipation and national development. Calls to decolonise knowledge have grown louder over "
    "the last decade, though intellectual decolonisation and decolonial theory are not necessarily "
    "synonymous. Those who emphasize epistemic power contend that the perpetuation of stereotypes "
    "and the devaluation of non-Western cultures are the primary oppressive mechanisms. "
    "Proponents of material political economy argue instead that the Global South’s oppressive "
    "mechanisms are rooted in history, economic structures, trade, debt, and resource inequality."
)

theme_card("4) Any other topic that fits with the broad theme of ‘Future of Development Studies’",
    "Traditional discussions of development studies may seem out of date given rapid changes "
    "within the global economy, technological advances, and geopolitics. This theme invites "
    "papers on new topics set to re-shape the parameters of the field, including geopolitics "
    "and development, the green transition, and artificial intelligence. These papers must make "
    "clear how they fit the ‘Future of Development Studies’ rather than just the future "
    "of development itself."
)

pdf.ln(2)
sec_head("Instructions for What to Send")
instr_box(
    "We will need three documents from all participants: 1) An extended abstract; 2) A short "
    "2-page CV; and 3) A writing sample (ideally a chapter of a PhD thesis or published journal "
    "article, but work-in-progress is acceptable). Please send these documents to Pritish Behuria "
    "(Pritish.behuria@manchester.ac.uk) by 30 September, 2026. Extended abstracts should follow "
    "the guidance below and should clearly state the main contributions of the paper. Abstracts "
    "should be 750–1,000 words long. If accepted for the conference, we will request final "
    "versions of short papers (3,000–4,000 words) or full papers (6,000–8,000 words long) "
    "submitted by 15 January 2027. Papers must be submitted in order to attend the workshop "
    "and claim travel expenses."
)

divider()

sec_head("About the Conference", dark=True)
body_text(
    "The first Asia conference will be held in Bandung, Indonesia — the location of the 1955 "
    "Asia-Africa conference, which ultimately led to the establishment of the Non-Aligned Movement "
    "and the G77 group of nations. Our host is Padjadjaran University in Bandung. The workshop "
    "will be in April 2027 (date TBC). The conference will have three days of events. The first "
    "day will be dedicated to presentations for the ‘Future of Development Studies’ workshop, "
    "contributing to an edited volume or special issue in a leading development studies journal. "
    "The second day will include presentations by Indonesia-based early career scholars on "
    "work-in-progress. The third day will provide focused support for early career researchers "
    "(academic article writing, journal selection, grant applications and career opportunities)."
)

if pdf.get_y() > 220:
    pdf.add_page()

y_grid = pdf.get_y()
card_w = (CW - 8) / 3
grid_data = [
    ("Eligibility",
     "Participants must be based at a university or HEI in Asia/Africa. Participants must have "
     "been awarded a PhD after 1 October 2017 (with flexibility for career breaks) or be "
     "currently enrolled in a PhD at a HEI in the Global South."),
    ("Funding",
     "Supported by the British Academy Writing Workshop grant (IWW25/100268), this project "
     "will fund return flights (from within Asia) and accommodation for three nights in "
     "Indonesia for all participants."),
    ("Output",
     "Outputs will form an edited collection or special issue comprising entirely early-career "
     "scholars based in Asia and Africa. The collection will be submitted to a prestigious "
     "academic press; the special issue to a leading development studies journal."),
]
max_h = 0
for i, (title, text) in enumerate(grid_data):
    pdf.set_y(y_grid)
    h = info_card(title, text, LM + i * (card_w + 4), card_w)
    max_h = max(max_h, h)

pdf.set_y(y_grid + max_h + 6)
divider()

# ── GUIDANCE ──────────────────────────────────────────────────────────────────
if pdf.get_y() > 230:
    pdf.add_page()

y0 = pdf.get_y()
pdf.set_fill_color(*BROWN_DK)
pdf.rect(LM, y0, CW, 22, style='F')
pdf.set_xy(LM + 5, y0 + 4)
pdf.set_font('Helvetica', 'B', 10.5)
pdf.set_text_color(*WHITE)
pdf.multi_cell(CW - 10, 5.5,
    "Guidance on Writing an Extended Abstract for an International Workshop or Journal")
pdf.set_xy(LM + 5, y0 + 15)
pdf.set_font('Helvetica', 'I', 8)
pdf.set_text_color(200, 200, 200)
pdf.cell(CW - 10, 4, "A guide for early career researchers in International Development Studies")
pdf.set_y(y0 + 27)


def block_what_it_is():
    pdf.set_x(LM + 5)
    pdf.set_font('Helvetica', '', 9)
    pdf.set_text_color(*TEXT)
    pdf.multi_cell(CW - 10, 4.5,
        "An extended abstract (750–1,000 words) is not a summary of work in progress. "
        "It is a condensed argument. Reviewers use it to decide whether your paper fits the "
        "programme. They need to see a clear question, a stated position, and evidence of "
        "intellectual rigour — not a tour of the terrain you plan to explore.")
    pdf.ln(2)


def block_must_contain():
    items = [
        "A title that implies a claim — not “Inequality in Southeast Asia” but "
        "“Why service-led growth has not reduced inequality in Vietnam.” The title should signal an argument.",
        "A research question. State it explicitly, in one sentence. Everything else follows from it.",
        "Engagement with theory and existing literature. Name the debate. Identify the gap. "
        "3–4 precise references are enough, but they must be present.",
        "A methodology statement. What data? What method? Why appropriate? 2–3 sentences.",
        "A thesis or working hypothesis. State your argument. Early-stage papers may not have "
        "final results, but they must have a position.",
    ]
    for item in items:
        by = pdf.get_y()
        pdf.set_fill_color(*ORANGE)
        pdf.rect(LM + 7, by + 1.5, 2, 2, style='F')
        pdf.set_xy(LM + 12, by)
        pdf.set_font('Helvetica', '', 9)
        pdf.set_text_color(*TEXT)
        pdf.multi_cell(CW - 17, 4.3, item)
        pdf.ln(0.5)
    pdf.ln(2)


def block_avoid():
    pdf.set_x(LM + 5)
    pdf.set_font('Helvetica', '', 9)
    pdf.set_text_color(*TEXT)
    pdf.multi_cell(CW - 10, 4.5,
        "“This paper examines...” is not a thesis. “This paper argues that...” is. "
        "Description signals a paper without a contribution.\n\n"
        "Avoid literature omission. An abstract with no theoretical grounding signals a thin contribution.")
    pdf.ln(2)


def block_headings():
    tags = ["Title", "Research Question(s)",
            "Theoretical Framework and Existing Literature",
            "Methodology", "Argument / Working Thesis", "Expected Contribution"]
    x0 = LM + 5
    row_y = pdf.get_y() + 1
    x = x0
    gap = 3
    th = 5.5
    for tag in tags:
        pdf.set_font('Helvetica', '', 8)
        tw = pdf.get_string_width(tag) + 6
        if x + tw > LM + CW - 5:
            row_y += th + gap
            x = x0
        pdf.set_fill_color(*BROWN_DK)
        pdf.rect(x, row_y, tw, th, style='F')
        pdf.set_xy(x + 2, row_y + 0.5)
        pdf.set_text_color(*WHITE)
        pdf.cell(tw - 4, th - 0.5, tag)
        x += tw + gap
    pdf.set_y(row_y + th + 5)


def block_checklist():
    items = [
        "Title implies a claim, not a topic",
        "Research question stated in one sentence",
        "3–4 key references named and engaged",
        "Methodology identified and briefly justified",
        "Thesis or working hypothesis stated explicitly",
        "Expected contribution stated explicitly",
    ]
    for item in items:
        by = pdf.get_y()
        pdf.set_fill_color(*ORANGE)
        pdf.rect(LM + 7, by + 1.5, 2.5, 2.5, style='F')
        pdf.set_xy(LM + 12, by)
        pdf.set_font('Helvetica', '', 9)
        pdf.set_text_color(*TEXT)
        pdf.cell(CW - 17, 5, item)
        pdf.set_draw_color(238, 227, 208)
        pdf.line(LM + 5, by + 5.5, LM + CW - 5, by + 5.5)
        pdf.ln(0.5)
    pdf.ln(3)


guidance_block("What it is", block_what_it_is)
guidance_block("What it must contain", block_must_contain)
guidance_block("What to avoid", block_avoid)
guidance_block("Headings to use in the extended abstract", block_headings)
guidance_block("Checklist before submission", block_checklist)

# ── Save ───────────────────────────────────────────────────────────────────────
out = os.path.join(BASE, 'call-for-papers.pdf')
pdf.output(out)
print(f"Saved: {out}")
