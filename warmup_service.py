# build a warmup class here



class Warmup:
    def __init__(
        target_daily_send_vol = 650000,
        number_of_ips = 2,
        initial_per_ip_vol = 50,
        number_engaged_users = 500000,
        warmup_factor = 1.5,
        max_warmup_schedule_length = 50,
    ):
        self.target_daily_send_vol = target_daily_send_vol
        self.number_of_ips = number_of_ips
        self.initial_per_ip_vol = initial_per_ip_vol
        self.number_engaged_users = number_engaged_users
        self.warmup_factor = warmup_factor
        self.max_warmup_schedule_length = max_warmup_schedule_length
        self.current_day = 1
        self.overrides = {}
        self.factor_overrides = []
        self.schedule = {}
        self.end_day = -1

    def set_current_day(day: int):
        self.current_day = day

    def get_current_day():
        return self.current_day

    def build_schedule():
        for day in range(1, self.max_warmup_schedule_length + 1):
            if day < current_day:
                assert day in self.schedule
            else:
                if day == 1:
                    emails = self.initial_per_ip_vol * self.initial_per_ip_vol
                else:
                    warmup_factor = self.warmup_factor
                    for start_day, end_day, factor in self.factor_overrides:
                        if start_day <= day <= end_day:
                            warmup_factor = factor
                            break
                    if day in self.overrides:
                        emails = self.overrides[day]
                    else:
                        emails = self.schedule[day - 1] * warmup_factor
                if emails >= target_daily_send_vol:
                    emails = target_daily_send_vol
                    self.schedule[day] = emails
                    self.end_day = day
                    break
                else:
                    self.schedule[day] = emails
        if self.end_day == -1:
            self.end_day = day
        assert self.schedule[self.end_day] == target_daily_send_vol
    
    def get_schedule():
        return self.schedule

    def add_override(day, emails):
        self.overrides[day] = emails

    def add_factor_override(start_day, end_day, factor):
        self.factor_overries.append((start_day, end_day, factor))
    
