'''
Suppose you have a set of activities with start and end times and you want to 
select a maximum subset of non-overlapping activities. A greedy algorithm for this problem would work as follows:

Sort the activities in ascending order based on their end times.
Select the first activity in the sorted list.
For each subsequent activity in the sorted list, select it if its start time is after the end time of the previously selected activity.
'''


def activity_selection(activities):
    activities.sort(key=lambda x: x[1])
    result = [activities[0]]
    for activity in activities[1:]:
        if activity[0] >= result[-1][1]:
            result.append(activity)
    return result

activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
print(activity_selection(activities))
# Output: [(1, 4), (5, 7), (8, 11), (12, 16)]


'''
In the above code, we sort the activities in ascending order based on their end times and then loop through them. 
We select the first activity and then for each subsequent activity, we check if its start time is after the end time of the
previously selected activity. If it is, we add it to the 
list of selected activities. The resulting list represents the maximum subset of non-overlapping activities.
'''
