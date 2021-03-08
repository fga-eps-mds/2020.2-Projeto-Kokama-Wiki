let member_username_name = {
    aluzianobriceno: "Ana Júlia",
    andrelucax: "André Lucas",
    SFernandoS: "Fernando Vargas",
    laispa: "Lais Portela",
    leomedeiros1: "Leonardo Medeiros",
    lievertom: "Lieverton Silva",
    nickby2: "Lucas Rodrigues",
    luisgaboardi: "Luís Guilherme",
    LightZX: "Luiz Gustavo",
    WelisonR: "Welison Regis",
};

/*
    Automatically download json file with informations about issues.
    Informations about issue: name, url, assigns and points.
    The result of this script is used by "planning.py" to generate scrum documents.
    
    IMPORTANT: it's necessary to install zenhub to define and retrieve issue points.

    How to use it:
    - Copy all the code;
    - Browse to an issues page (open or closed);
    - Open the browser console (F12);
    - Paste this code.

    Results:
    - The execution of this script will generate a json file with issues details.
*/
class GithubIssues {
    constructor() {
        this.base_url = "https://github.com/";
        this.issues_html = document.querySelectorAll("[data-id]");
        this.issues = this.build_issues(this.issues_html);
    }

    build_issues(issues_html) {
        const issues = [];

        issues_html.forEach((issue_html) => {
            let issue_url = this.get_issue_url(issue_html);
            let issue_text = this.get_issue_text(issue_html);
            let issue_assigns_array = this.get_issue_assigns(issue_html);
            let issues_points = this.get_issue_points(issue_html);

            let issue = {
                text: issue_text,
                url: issue_url,
                assigns: issue_assigns_array,
                points: issues_points,
            };

            issues.push(issue);
        });

        return issues;
    }

    get_issue_url(issue_html) {
        let issue_link_html = issue_html.querySelector('[id$="_link"]');
        let issue_url = this.base_url + issue_link_html.getAttribute("href");

        return issue_url;
    }

    get_issue_text(issue_html) {
        let issue_link_html = issue_html.querySelector('[id$="_link"]');
        let issue_text = issue_link_html.innerHTML;

        return issue_text;
    }

    get_issue_assigns(issue_html) {
        let issue_assigns_html = issue_html.querySelectorAll('[aria-label^="Assigned to"]')[0];
        let issue_assigns_string = issue_assigns_html
            .getAttribute("aria-label")
            .replace("Assigned to ", "")
            .replace(", and ", ", ")
            .replace("and ", ", ");
        let issue_assigns_array = issue_assigns_string.split(",").map((issue_assign) => {
            let assign = issue_assign.trim();
            let name = member_username_name[assign];

            let assign_info = {
                assign: assign || "Não definido",
                name: name || "Não definido",
            };

            return assign_info;
        });

        return issue_assigns_array;
    }

    get_issue_points(issue_html) {
        let issue_points_html = issue_html.querySelector(".zh-estimate-badge");

        let issue_points = 0;
        if (issue_points_html) {
            issue_points = Number.parseInt(issue_points_html.innerHTML);
        }

        return issue_points;
    }
}

/*
    Script to download an object as json from browser
*/
class DownloadIssueData {
    constructor() {
        this.all_issues = new GithubIssues();
        this.download(this.all_issues.issues);
    }

    download(data) {
        if (!data) {
            console.error("Console.save: Nenhum dado disponível");
            return;
        }

        let filename = "issues.json";

        if (typeof data === "object") {
            data = JSON.stringify(data, undefined, 4);
        }

        var blob = new Blob([data], { type: "text/json" }),
            e = document.createEvent("MouseEvents"),
            a = document.createElement("a");

        a.download = filename;
        a.href = window.URL.createObjectURL(blob);
        a.dataset.downloadurl = ["text/json", a.download, a.href].join(":");
        e.initMouseEvent("click", true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        a.dispatchEvent(e);
    }
}

new DownloadIssueData();
