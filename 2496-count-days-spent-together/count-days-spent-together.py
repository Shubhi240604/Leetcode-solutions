class Solution:

  def countDaysTogether(
      self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
  ) -> int:
    days_in_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def to_day_of_year(date_str: str) -> int:
      month = int(date_str[:2])
      day = int(date_str[3:])
      return sum(days_in_months[:month]) + day

    arrive_a = to_day_of_year(arriveAlice)
    leave_a = to_day_of_year(leaveAlice)
    arrive_b = to_day_of_year(arriveBob)
    leave_b = to_day_of_year(leaveBob)

    start_overlap = max(arrive_a, arrive_b)
    end_overlap = min(leave_a, leave_b)

    return max(0, end_overlap - start_overlap + 1)
