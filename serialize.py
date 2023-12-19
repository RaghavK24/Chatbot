def serialize_user(user):
    return {
        "user_id": user.user_id,
        "email": user.email,
        # Exclude password for security reasons
        # "password": user.password,
        # Add other fields as needed
    }


def serialize_counselling(counselling):
    return {
        "counselling_id": counselling.counselling_id,
        "type": counselling.type,
        "description": counselling.description,
        # Add other fields as needed
    }

def serialize_location(district, state):
    return {
        "district_id": district.name,
        "state_id": state.name,
        "district_name": district.name,
        "state_name": state.name,
        # Add other fields as needed
    }


def serialize_experience(experience):
    return {
        "name": experience.name,
        # Add other fields as needed
    }


def serialize_job_preference(job_preference):
    return {
        "preference_id": job_preference.preference_id,
        "user_id": job_preference.user_id,
        "job_type": job_preference.job_type,
        "location": job_preference.location,
        "industry": job_preference.industry,
        # Add other fields as needed
    }


def serialize_job_type(job_type):
    return {
        "name": job_type.name,
        # Add other fields as needed
    }


def serialize_jobs_for_women(job_for_women):
    return {
        "job_id": job_for_women.job_id,
        "job_title": job_for_women.job_title,
        "job_description": job_for_women.job_description,
        "is_active": job_for_women.is_active,
        "created_on": job_for_women.created_on,
        "job_type": job_for_women.job_type,
        "qualification": job_for_women.qualification,
        "experience": job_for_women.experience,
        "location": job_for_women.location,
        # Add other fields as needed
    }


def serialize_jobs(job):
    return {
        "job_id": job.job_id,
        "job_title": job.job_title,
        "job_description": job.job_description,
        "is_active": job.is_active,
        "created_on": job.created_on,
        "job_type": job.job_type,
        "qualification": job.qualification,
        "experience": job.experience,
        "location": job.location,
        # Add other fields as needed
    }


def serialize_qualification(qualification):
    return {
        "name": qualification.name,
        # Add other fields as needed
    }


def serialize_skills(skill):
    return {
        "skill_id": skill.skill_id,
        "skill_name": skill.skill_name,
        "description": skill.description,
        # Add other fields as needed
    }



def serialize_user_history(user_history):
    return {
        "history_id": user_history.history_id,
        "user_id": user_history.user_id,
        "job_viewed": user_history.job_viewed,
        "course_taken": user_history.course_taken,
        "counselling_attended": user_history.counselling_attended,
        # Add other fields as needed
    }