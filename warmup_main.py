import math

def main():

    target_daily_send_vol = 650000
    number_of_ips = 2
    initial_per_ip_vol = 50
    number_engaged_users = 500000
    starting_send_vol = 0
    warmup_factor = 1.5
    max_warmup_schedule_length = 50

    assert warmup_factor > 1, "Your warmup-factor ({warmup_factor}x) is <= 1 -- your daily sends will never increase!"
    assert starting_send_vol >= 0, "You cannot choose a negative initial send volume."
    assert number_of_ips >= 1, "You must have at least one IP."
    assert target_daily_send_vol > 0, "Your target daily send volume must be > 0."

    if starting_send_vol == 0:
        daily_send_vol = number_of_ips * initial_per_ip_vol
        warmup_schedule = [daily_send_vol]
    else:
        daily_send_vol = starting_send_vol

    required_campaigns_count = 1
    campaign_total_sends = daily_send_vol

    while (daily_send_vol < target_daily_send_vol):
        daily_send_vol = math.floor(daily_send_vol * warmup_factor)
        warmup_schedule.append(daily_send_vol)
        campaign_total_sends = campaign_total_sends + daily_send_vol
        if campaign_total_sends >= number_engaged_users:
            required_campaigns_count = required_campaigns_count + 1
            campaign_total_sends = campaign_total_sends - number_engaged_users 

        if len(warmup_schedule) > max_warmup_schedule_length:
            print(f"warmup schedule is longer than {max_warmup_schedule_length} days, but target daily send volume {target_daily_send_vol} has not been reached!")
            break

    print(f"warmup_schedule: {warmup_schedule}")
    print(f"number of campaigns required: {required_campaigns_count}")

if __name__ == '__main__':
  main()

