# AdressBook().data= {str:Record(),}
# Record() .name | .phones | .bday
# phones=[Phone(Field),]
# Field() .value #last stop


def search(what, where):
    results = []
    # for name, record in AdressBook().data.items()
    for name, record in where.data.items():
        record_text = (
            f'{name}:{", ".join(ph.value for ph in record.phones)};'
        )
        if record.bday:
            record_text = (
                f'{name}:{", ".join(ph.value for ph in record.phones)}; {record.bday.value}'
            )
        if what.lower() in record_text.lower():
            results.append(record_text)
    if results == []:
        return 'no match! type "search" again and try another pattern'
    return "\n".join(results)
