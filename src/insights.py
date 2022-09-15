from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    unique_job_list = dict()

    for jobs in jobs_list:
        if jobs["job_type"] in unique_job_list:
            unique_job_list[jobs["job_type"]] += 1
        else:
            unique_job_list[jobs["job_type"]] = 1
    return unique_job_list


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for item in jobs:
        if item["job_type"] == job_type:
            filtered_jobs.append(item)
    return filtered_jobs


def get_unique_industries(path):
    jobs_list = read(path)
    unique_industry_list = []

    for jobs in jobs_list:
        industries = jobs["industry"]
        if industries not in unique_industry_list and industries != "":
            unique_industry_list.append(industries)
    return unique_industry_list


def filter_by_industry(jobs, industry):
    filtered_industries = []
    for item in jobs:
        if item["industry"] == industry:
            filtered_industries.append(item)
    return filtered_industries


def get_max_salary(path):
    jobs_list = read(path)
    max_salary = 0

    for jobs in jobs_list:
        max_salary_in_list = jobs["max_salary"]
        try:
            conv = int(max_salary_in_list)
            if conv > max_salary:
                max_salary = conv
        except Exception:
            pass
    return max_salary
# except Exception tirado de
# https://stackoverflow.com/questions/54948548/what-is-wrong-with-using-a-bare-except


def get_min_salary(path):
    jobs_list = read(path)
    min_salary = []

    for jobs in jobs_list:
        min_salary_in_list = jobs["min_salary"]
        if min_salary_in_list and min_salary_in_list.isdigit():
            min_salary.append(int(min_salary_in_list))
    return min(min_salary)


def matches_salary_range(job, salary):

    # isinstance pego de
    # https://pythonguides.com/python-check-if-the-variable-is-an-integer/

    # job.keys() "opcional"
    if (
        "min_salary" in job
        and "max_salary" in job
        and isinstance(job["min_salary"], int)
        and isinstance(job["max_salary"], int)
        and job["min_salary"] <= job["max_salary"]
        and isinstance(salary, int)
    ):
        return job["min_salary"] <= salary <= job["max_salary"]
    else:
        raise ValueError('Error')


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
