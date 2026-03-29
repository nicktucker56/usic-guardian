#!/usr/bin/env python3
"""Batch add new anchors to USIC Guardian"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.anchor_manager import AnchorManager, SemanticAnchor

def add_anchors(manager):
    """Add new anchors"""
    
    new_anchors = [
        # Health anchors
        ("health_sleep", "Sleep Issues", 
         ["can't sleep", "insomnia", "tired", "exhausted", "sleep problems", "wake up tired"],
         0.60, 0.32,
         ["Sleep is foundational. What's keeping you awake?", "Rest is essential. What would help you relax?"],
         "health", "sleep", 0.5),
        
        ("health_anxiety", "Anxiety", 
         ["anxious", "worry", "panic", "racing thoughts", "nervous", "can't relax"],
         0.55, 0.38,
         ["Anxiety is real. What's the worry telling you?", "Those feelings are valid. What would help you feel grounded?"],
         "health", "anxiety", 0.6),
        
        ("health_depression", "Depression", 
         ["depressed", "sad", "hopeless", "no joy", "empty", "nothing matters"],
         0.35, 0.58,
         ["Depression lies. What would help you feel seen?", "You're not alone in this. What's one small thing that brings comfort?"],
         "health", "depression", 0.8),
        
        # Finance anchors
        ("finance_debt", "Debt Stress", 
         ["debt", "owe", "bills", "can't pay", "money stress", "credit card"],
         0.50, 0.42,
         ["Financial stress is heavy. What's the most pressing concern?", "What would ease your mind?"],
         "finance", "debt", 0.6),
        
        ("finance_job_loss", "Job Loss", 
         ["lost job", "unemployed", "laid off", "no income", "fired", "terminated"],
         0.48, 0.45,
         ["Job loss is a shock. What do you need to stabilize?", "This is hard. What's one thing you can do today?"],
         "finance", "employment", 0.7),
        
        ("finance_retirement", "Retirement", 
         ["retirement", "savings", "not enough", "late start", "retire"],
         0.55, 0.38,
         ["Planning for the future is wise. What's your biggest question?", "What would make you feel secure?"],
         "finance", "retirement", 0.5),
        
        # Education anchors
        ("edu_student", "Student Stress", 
         ["student", "studying", "exam", "grade", "school", "college", "university"],
         0.62, 0.30,
         ["Learning is challenging. What's hardest right now?", "You're doing better than you think."],
         "education", "student", 0.5),
        
        ("edu_teacher", "Teacher Burnout", 
         ["teacher", "teaching", "classroom", "students", "educator"],
         0.55, 0.38,
         ["Teaching is demanding. What's weighing on you?", "You give so much. What fills you back up?"],
         "education", "teacher", 0.6),
        
        ("edu_motivation", "Motivation", 
         ["no motivation", "can't focus", "procrastinate", "unmotivated"],
         0.58, 0.35,
         ["Motivation comes and goes. What usually helps you focus?", "What's one small thing you can do?"],
         "education", "motivation", 0.5),
    ]
    
    count = 0
    for anchor_data in new_anchors:
        anchor_id, name, keywords, r, c, responses, category, subcategory, intensity = anchor_data
        existing = manager.get_anchor(anchor_id)
        if not existing:
            anchor = SemanticAnchor(
                id=anchor_id,
                name=name,
                keywords=keywords,
                receptivity=r,
                collapse=c,
                responses=responses,
                category=category,
                subcategory=subcategory,
                intensity=intensity
            )
            manager.add_anchor(anchor)
            print(f"✅ Added anchor: {anchor_id}")
            count += 1
        else:
            print(f"⚠️ Anchor {anchor_id} already exists")
    
    return count

if __name__ == "__main__":
    manager = AnchorManager()
    print(f"Current anchors: {len(manager.anchors)}")
    count = add_anchors(manager)
    print(f"\n✅ Added {count} new anchors")
    print(f"Total anchors: {len(manager.anchors)}")
