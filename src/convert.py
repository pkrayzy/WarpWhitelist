from src import (
    info,
    ip_pattern, 
    domain_pattern, 
    replace_pattern
)

def convert_to_domain_list(white_content: str) -> list[str]:
    white_domains = set()
    
    extract_domains(white_content, white_domains)
    info(f"Number of whitelisted domains: {len(white_domains)}")

    final_domains = sorted(list(white_domains))
    info(f"Number of final domains: {len(final_domains)}")

    return final_domains

def extract_domains(content: str, domains: set[str]) -> None:
    for line in content.splitlines():
        if line.startswith(("#", "!", "/")) or line == "":
            continue

        cleaned_line = line.lower().strip().split("#")[0].split("^")[0].replace("\r", "")
        domain = replace_pattern.sub("", cleaned_line, count=1)
        try:
            domain = domain.encode("idna").decode("utf-8", "replace")
            if domain_pattern.match(domain) and not ip_pattern.match(domain):
                domains.add(domain)
        except Exception:
            pass
