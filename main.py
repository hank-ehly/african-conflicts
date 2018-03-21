import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def main():
    original_column_names = ['ACTOR1', 'ACTOR1_ID', 'ACTOR2', 'ACTOR2_ID', 'ACTOR_DYAD_ID', 'ADMIN1', 'ADMIN2',
                             'ADMIN3', 'ALLY_ACTOR_1', 'ALLY_ACTOR_2', 'COUNTRY', 'EVENT_DATE', 'EVENT_ID_CNTY',
                             'EVENT_ID_NO_CNTY', 'EVENT_TYPE', 'FATALITIES', 'GEO_PRECISION', 'GWNO', 'INTER1',
                             'INTER2', 'INTERACTION', 'LATITUDE', 'LOCATION', 'LONGITUDE', 'NOTES', 'SOURCE',
                             'TIME_PRECISION', 'YEAR']
    names = list(map(lambda name: name.lower(), original_column_names))
    df = pd.read_csv('african_conflicts.csv', encoding='latin-1', names=names)
    df.year = df.year.apply(pd.to_numeric, errors='ignore')

    zimbabwe_conflicts_by_year = df[df.country == 'Zimbabwe'].sort_values(by='year')

    # Number of conflicts by year in Zimbabwe
    # Looks like number of conflicts is greater during presidential elections
    # vcs = zimbabwe_df.year.value_counts(sort=False)
    # vc_keys = list(vcs.keys())
    # plt.plot(vc_keys, vcs)
    # xtick_names = list(map(lambda k: '\'%s' % str(k)[2:], vc_keys))
    # plt.xticks(vc_keys, xtick_names, size='small')
    # plt.xlabel('Year (%s ~ %s)' % (min(vc_keys), max(vc_keys)))
    # plt.ylabel('Number of conflicts')
    # plt.title('Zimbabwe')

    # Check if there is a correlation between year and actor1
    years = zimbabwe_conflicts_by_year.year
    actors = zimbabwe_conflicts_by_year.actor1

    years_unique = years.unique()
    years_abbrev = list(map(lambda y: '\'%s' % str(y)[2:], years_unique))

    unique_actor_names, actor_idx = np.unique(actors, return_inverse=True)

    plt.scatter(rand_jitter(years), rand_jitter(actor_idx), alpha=0.1)
    plt.xticks(years_unique, years_abbrev)
    plt.yticks(np.unique(actor_idx), unique_actor_names, size='small', rotation=20)
    plt.show()


def rand_jitter(arr):
    stdev = .01 * (max(arr) - min(arr))
    return arr + np.random.randn(len(arr)) * stdev


if __name__ == '__main__':
    main()
