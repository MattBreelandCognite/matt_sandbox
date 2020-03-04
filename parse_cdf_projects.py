import csv
import json


def search_cdf_project_list(cdf_project_file, search_strings):

    with open('./cdf_projects.json') as f:
        all_projects = json.load(f)
        project_list = []
        for project in all_projects:
            for item in search_strings:
                if item in project['urlName']:
                    project_list.append(project['urlName'])

        return project_list


def export_list_to_csv(my_list, csv_file_name):
    with open(csv_file_name, 'w') as myfile:
        wr = csv.writer(myfile)
        for item in my_list:
            # wrap each string into a list to avoid splitting each character into a cell
            wr.writerow([item])


if __name__ == '__main__':
    # TODO: populate cdf_project_file from https://project-id-name-app.cognite.ai/
    cdf_project_input_file = './cdf_projects.json'
    cdf_project_output_file = './aker_bp_cdf_projects.csv'
    search_strings = ['akerbp', 'akbp']

    project_list = search_cdf_project_list(cdf_project_input_file, search_strings)
    export_list_to_csv(project_list, cdf_project_output_file)
    print('{} project names found containing {} and written to {}'.format(
        len(project_list), search_strings, cdf_project_output_file))
