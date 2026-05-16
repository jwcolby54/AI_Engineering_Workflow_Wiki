from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle, ListFlowable, ListItem
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

OUTPUT = "AI_Engineering_Workflow_Why_And_How.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=letter,
    leftMargin=1.1 * inch,
    rightMargin=1.1 * inch,
    topMargin=1.0 * inch,
    bottomMargin=1.0 * inch,
    title="AI Engineering Workflow - Why AI Work Needs A Durable Record",
    author="John Colby",
)

styles = getSampleStyleSheet()

DARK = colors.HexColor("#1a1a1a")
ACCENT = colors.HexColor("#2c5f8a")
RULE = colors.HexColor("#cccccc")
CODE_BG = colors.HexColor("#f5f5f5")

title_style = ParagraphStyle(
    "DocTitle",
    parent=styles["Title"],
    fontSize=22,
    leading=28,
    textColor=ACCENT,
    spaceAfter=6,
    fontName="Helvetica-Bold",
    alignment=TA_CENTER,
)
subtitle_style = ParagraphStyle(
    "DocSubtitle",
    parent=styles["Normal"],
    fontSize=12,
    leading=16,
    textColor=DARK,
    spaceAfter=8,
    fontName="Helvetica-Oblique",
    alignment=TA_CENTER,
)
h2_style = ParagraphStyle(
    "H2",
    parent=styles["Heading2"],
    fontSize=13,
    leading=18,
    textColor=ACCENT,
    spaceBefore=18,
    spaceAfter=6,
    fontName="Helvetica-Bold",
)
body_style = ParagraphStyle(
    "Body",
    parent=styles["Normal"],
    fontSize=10.5,
    leading=16,
    textColor=DARK,
    spaceAfter=8,
    fontName="Helvetica",
)
bullet_style = ParagraphStyle(
    "Bullet",
    parent=body_style,
    leftIndent=18,
    spaceAfter=4,
)
step_style = ParagraphStyle(
    "Step",
    parent=body_style,
    leftIndent=18,
    spaceAfter=3,
)
rule_style = ParagraphStyle(
    "Rule",
    parent=body_style,
    fontSize=10.5,
    leading=16,
    fontName="Helvetica-BoldOblique",
    textColor=DARK,
    spaceAfter=8,
)
byline_style = ParagraphStyle(
    "Byline",
    parent=body_style,
    fontSize=10,
    textColor=colors.HexColor("#555555"),
    spaceBefore=24,
    spaceAfter=4,
)

def hr():
    return HRFlowable(width="100%", thickness=0.5, color=RULE, spaceAfter=14, spaceBefore=6)

def h2(text):
    return Paragraph(text, h2_style)

def body(text):
    return Paragraph(text, body_style)

def bullets(items):
    return ListFlowable(
        [ListItem(Paragraph(i, bullet_style), bulletColor=ACCENT) for i in items],
        bulletType="bullet",
        leftIndent=18,
        bulletFontSize=8,
        spaceAfter=8,
    )

def numbered(items):
    return ListFlowable(
        [ListItem(Paragraph(i, step_style)) for i in items],
        bulletType="1",
        leftIndent=18,
        bulletFontSize=10,
        spaceAfter=8,
    )

severity_data = [
    ["Severity", "Meaning"],
    ["BLOCKING", "Must be resolved before forward progress."],
    ["MAJOR", "Should be resolved before implementation; Human waiver required if left open."],
    ["MINOR", "Recommended improvement; does not block."],
    ["FUTURE", "Valid but out of scope for this session."],
]

severity_table = Table(
    severity_data,
    colWidths=[1.2 * inch, 4.8 * inch],
    hAlign="LEFT",
)
severity_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), ACCENT),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 10),
    ("LEADING", (0, 0), (-1, -1), 14),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#f9f9f9"), colors.white]),
    ("GRID", (0, 0), (-1, -1), 0.4, RULE),
    ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
]))

story = []

# Title block
story.append(Paragraph("AI Engineering Workflow", title_style))
story.append(Paragraph("Where AI chats become project records.", subtitle_style))
story.append(Spacer(1, 0.32 * inch))
story.append(h2("Why AI Work Needs A Durable Record"))

# Intro
story.append(body(
    "AI can help you think faster than any tool most of us have ever used."
))
story.append(body(
    "It can help shape an idea, challenge assumptions, draft a plan, inspect code, propose "
    "architecture, write public copy, and find problems you did not know to look for. But there "
    "is a catch: the useful work often lives inside a chat transcript."
))
story.append(body(
    "That feels fine while the conversation is active. It feels much worse later."
))
story.append(body(
    "You come back to a long thread and try to remember which version of the idea was best. "
    "You scroll past abandoned branches, half-decisions, useful objections, stale assumptions, "
    "and paragraphs that felt brilliant at the time but are now hard to place. If you used more "
    "than one AI tool, the problem gets worse: the human becomes the copy/paste bridge between systems."
))
story.append(body("AI Engineering Workflow exists to solve that problem."))
story.append(body(
    "It turns AI-assisted work into a durable project record: what was proposed, what was "
    "challenged, what changed, what was approved, and what should happen next."
))
story.append(body(
    "<b>The point is not to make AI autonomous. The point is to make AI collaboration legible.</b>"
))
story.append(hr())

# The Core Idea
story.append(h2("The Core Idea"))
story.append(body(
    "AI Engineering Workflow is a manual-first process for one human operator working with "
    "two agentic AI tools. The known working combination is Claude.Code plus Codex. Other "
    "agentic tools may work, but they are not yet proven in this project."
))
story.append(body(
    "The workflow uses a shared Markdown record as the source of truth. Chat is the workspace. "
    "The Workflow Record is the durable state."
))
story.append(body("At a high level:"))
story.append(numbered([
    "The Human defines the objective.",
    "AI_1 proposes.",
    "AI_2 critiques with severity levels.",
    "The Human clarifies priorities and remains final authority.",
    "AI_1 revises.",
    "AI_2 reviews again.",
    "Scope freezes.",
    "The Human approves the gate.",
    "Implementation or drafting proceeds.",
    "Validation is recorded.",
]))
story.append(body(
    "This is familiar engineering discipline applied to AI-assisted work: proposal, critique, "
    "revision, approval, execution, validation."
))
story.append(hr())

# What Problem It Solves
story.append(h2("What Problem It Solves"))
story.append(body("The workflow was created because ordinary AI chat has several failure modes:"))
story.append(bullets([
    "Good ideas get buried in long transcripts.",
    "Decisions blur together with speculation.",
    "Critiques get softened or lost during handoff.",
    "Scope changes silently.",
    "A later session cannot tell what was approved.",
    "One AI tool cannot reliably inherit the state of another.",
    "The human becomes the only durable transport layer between systems.",
]))
story.append(body(
    "AI Engineering Workflow moves the important state out of chat and into structured Markdown."
))
story.append(body("That simple shift changes the work."))
story.append(body(
    'Instead of asking, "What did we decide somewhere in that thread?" the record says what '
    "was proposed, what objections were raised, what changed, what is frozen, and what remains open."
))
story.append(hr())

# Why Two Agentic AIs
story.append(h2("Why Two Agentic AIs"))
story.append(body(
    "The current workflow assumes two agentic AI tools because the proposal and critique "
    "roles are intentionally separated."
))
story.append(body("AI_1 is responsible for proposing or revising."))
story.append(body("AI_2 is responsible for reviewing, challenging, and assigning severity."))
story.append(body(
    "The separation matters because single-model self-review can share the same assumptions "
    "as the original answer. A second agentic tool is not magic, and it does not guarantee "
    "correctness, but it creates useful friction. It makes disagreement cheaper. It gives "
    "the Human a clearer review surface."
))
story.append(body("The Human still decides."))
story.append(body(
    "The AIs are reasoning systems inside a governed process. They are not the authority."
))
story.append(hr())

# The Workflow Record
story.append(h2("The Workflow Record"))
story.append(body("The Workflow Record is the center of the system."))
story.append(body("It is a Markdown file that captures:"))
story.append(bullets([
    "objective", "current state", "human requirements", "constraints",
    "AI_1 proposal", "AI_2 critique", "human clarification", "AI_1 revision",
    "AI_2 final review", "concern severity", "scope freeze", "implementation gate",
    "validation requirements", "next action",
]))
story.append(body("The rule is simple:"))
story.append(Paragraph(
    '"If a decision is not in the Workflow Record, it did not happen in any durable sense."',
    rule_style
))
story.append(body(
    "This makes the record useful to the Human, to future AI sessions, and to any reviewer "
    "trying to understand how a decision was reached."
))
story.append(hr())

# Severity Levels
story.append(h2("Severity Levels"))
story.append(body("Review findings use four severity levels:"))
story.append(Spacer(1, 6))
story.append(severity_table)
story.append(Spacer(1, 8))
story.append(body(
    "This prevents all feedback from feeling equal. Some objections should stop the work. "
    "Some should improve it. Some should be recorded without derailing the current scope."
))
story.append(hr())

# Scope Freeze and Approval Gates
story.append(h2("Scope Freeze and Approval Gates"))
story.append(body(
    "One of the most important parts of the workflow is the scope freeze."
))
story.append(body(
    "AI tools are very good at expanding scope. They add useful-looking features, alternate "
    "framings, extra cases, and implementation details. Sometimes that is helpful. Sometimes "
    "it causes drift."
))
story.append(body(
    "The scope freeze records what is in scope and what is explicitly out of scope before "
    "implementation or drafting begins."
))
story.append(body("The implementation gate then records approval from:"))
story.append(bullets(["AI_1", "AI_2", "Human"]))
story.append(body("The Human approval is the one that matters most."))
story.append(body(
    "AI can recommend. AI can critique. AI can revise. But the Human decides whether "
    "the work is ready to proceed."
))
story.append(hr())

# What This Is Not
story.append(h2("What This Is Not"))
story.append(body("AI Engineering Workflow is not:"))
story.append(bullets([
    "a prompt collection",
    "a fully automated agent framework",
    "a replacement for human judgment",
    "a claim that AI output is automatically correct",
    "a claim that this has been proven at team scale",
]))
story.append(body(
    "It is a practical operating pattern for making AI-assisted work easier to review, "
    "resume, and trust."
))
story.append(hr())

# A Simple Example
story.append(h2("A Simple Example"))
story.append(body("<b>Without the workflow:</b>"))
story.append(body(
    "You brainstorm with an AI tool for an hour. The conversation is productive. Later, "
    "you try to recover the useful parts from the transcript. You remember there was a good "
    "objection somewhere, a better version of the thesis, and maybe a decision about scope, "
    "but now it is all mixed together."
))
story.append(body("<b>With the workflow:</b>"))
story.append(body(
    "The proposal goes into the record. The critique goes into the record. The Human's "
    "clarification goes into the record. The revision goes into the record. The approved "
    "scope and next action are explicit."
))
story.append(body(
    "The conversation still happens, but the work no longer disappears into the conversation."
))
story.append(hr())

# Why It Matters
story.append(h2("Why It Matters"))
story.append(body("AI-assisted work is moving from quick answers toward real projects."))
story.append(body(
    "Real projects need memory, review, state, and approval. They need a way to know what "
    "has been decided and what has not. They need a way to resume after a tool switch, a "
    "context reset, or a day away."
))
story.append(body("AI Engineering Workflow gives that process a simple form:"))
story.append(body(
    "plain Markdown, explicit roles, adversarial review, scope freeze, approval gates, "
    "and durable records."
))
story.append(body(
    "It is not heavy machinery. It is a way to stop treating chat as the project record."
))
story.append(hr())

# Current Status
story.append(h2("Current Status"))
story.append(body(
    "The workflow is public and documented at:"
))
story.append(Paragraph(
    '<a href="https://github.com/jwcolby54/AI_Engineering_Workflow_Wiki" color="#2c5f8a">'
    'https://github.com/jwcolby54/AI_Engineering_Workflow_Wiki</a>',
    body_style
))
story.append(body(
    "It is currently tested as a solo-human workflow using two agentic AI tools. "
    "The working combination is Claude.Code plus Codex. A natural next step would be "
    "broader use across other tool combinations and richer project examples."
))
story.append(hr())

# Byline
story.append(Paragraph("John Colby", byline_style))
story.append(Paragraph(
    "Builder of AI-assisted systems and author of AI Engineering Workflow.",
    ParagraphStyle("BylineDetail", parent=byline_style, spaceAfter=2)
))
story.append(Paragraph(
    '<a href="https://github.com/jwcolby54/AI_Engineering_Workflow_Wiki" color="#2c5f8a">'
    'github.com/jwcolby54/AI_Engineering_Workflow_Wiki</a>',
    ParagraphStyle("BylineLink", parent=byline_style, spaceAfter=2)
))
story.append(Paragraph(
    '<a href="https://www.linkedin.com/in/john-colby-1625b95/" color="#2c5f8a">'
    'linkedin.com/in/john-colby-1625b95</a>',
    ParagraphStyle("BylineLinkedIn", parent=byline_style, spaceAfter=0)
))

doc.build(story)
print(f"PDF written to {OUTPUT}")
