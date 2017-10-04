class Call(object):
    id = 1
    def __init__(self, caller_name, phone_number, time_of_call, reason):
        self.id = Call.id
        Call.id += 1
        self.caller_name = caller_name
        self.phone_number = phone_number
        self.time_of_call = time_of_call
        self.reason = reason

    def display_info(self):
        print "Unique ID:", self.id
        print "Caller Name:", self.caller_name
        print "Caller Phone Number:", self.phone_number
        print "Time of Call:", self.time_of_call
        print "Reason for Call:", self.reason
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0

    def add(self, caller_name, phone_number, time_of_call, reason):
        self.calls.append(Call(caller_name, phone_number, time_of_call, reason))
        return self

    def remove(self):
        self.calls.pop(0)
        return self

    def queue_info(self):
        for calls in self.calls:
            print "Name:", calls.caller_name
            print "Phone Number:", calls.phone_number
            print "ID:", calls.id
        print "Queue Length:", len(self.calls)
        return self

    def remove_number(self, number):
        for callers in self.calls:
            if callers.phone_number == number:
                self.calls.remove(callers)
        return self
        

center = CallCenter()
center.add('Dan Emunds', '769-1451', 16, 'Troubleshooting')
center.add('Evan Munz', '341-0138', 14, 'Broken Equipment')
center.add('Steve Compere', '979-7920', 9, 'Dead')
center.add('Paul Leo', '986-2410', 12, 'Too Far')
center.remove_number('341-0138')
center.remove_number('979-7920')
center.remove()
center.queue_info()


# for calls in center.calls:
#     print calls.phone_number




