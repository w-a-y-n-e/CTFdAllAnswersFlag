from CTFd.plugins import flags, register_plugin_assets_directory


class CTFdAllAnswersFlag(flags.BaseFlag):
    name = "all_answers"
    templates = {  # Nunjucks templates used for key editing & viewing
        "create": "/plugins/all_answers/assets/create.html",
        "update": "/plugins/all_answers/assets/edit.html",
        }

    @staticmethod
    def compare(chal_key_obj, provided):
    #Answers must be comma separated to be scored correctly
        saved = chal_key_obj.content.split(",")
        provided = provided.split(",")
        data = chal_key_obj.data
        if len(set(saved)) != len(set(provided)):
            return False
        if data == "case_insensitive":
            saved_stripped = set([s.strip().lower() for s in saved])
            provided_stripped = set([s.strip().lower() for s in provided])

            if saved_stripped == provided_stripped:
                return True
            else:
                return False
        else:
            saved_stripped = set([s.strip() for s in saved])
            provided_stripped = set([s.strip() for s in provided])
            if saved_stripped == provided_stripped:
                return True
            else:
                return False

flags.FLAG_CLASSES["all_answers"] = CTFdAllAnswersFlag

def load(app):
    register_plugin_assets_directory(app, base_path='/plugins/all_answers/assets/')