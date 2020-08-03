package {{base_package}}.service.impl;
import {{base_package}}.entity.{{entity}};
import {{base_package}}.exceptions.{{entity}}Exception;
import {{base_package}}.repositories.{{entity}}Repository;
import {{base_package}}.service.BaseService;
import {{base_package}}.exceptions.WErrorMessage;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

@Service
public class {{entity}}ServiceImpl implements BaseService<{{entity}}> {
    @Autowired
    private {{entity}}Repository dbRepository;

    public {{entity}} create({{entity}} entity) {
        return dbRepository.save(entity);
    }

    public {{entity}} findOne(Map<String, Object> filters) {
        throw new {{entity}}Exception(WErrorMessage.NOT_IMPLEMENTED.toString());
    }

    public {{entity}} findById(Long id) {
        return dbRepository.findOne(id.intValue());
    }

    public List<{{entity}}> findAll(Map<String, Object> filters) {
        throw new {{entity}}Exception(WErrorMessage.NOT_IMPLEMENTED.toString());
    }

    public {{entity}} save({{entity}} entity) {
        return dbRepository.save(entity);
    }

    public  {{entity}}  update({{entity}} entity) {
       return dbRepository.save(entity);
    }

    public void delete({{entity}} entity) {
        dbRepository.delete(entity);
    }

    public void deleteById(Long id) {
         dbRepository.delete(id.intValue());
    }
}